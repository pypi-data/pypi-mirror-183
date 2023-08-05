# This package describes the Postgres tables Robotoff is writing to.
import datetime
import functools
import uuid
from typing import Iterable

import peewee
from playhouse.postgres_ext import BinaryJSONField, PostgresqlExtDatabase
from playhouse.shortcuts import model_to_dict

from robotoff import settings

db = PostgresqlExtDatabase(
    settings.POSTGRES_DB,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=5432,
    autoconnect=False,
)


def with_db(fn):
    """Run function inside a SQL transaction."""

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        with db:
            # use atomic transaction to avoid falling in a bad state
            # (error in the main transaction)
            return fn(*args, **kwargs)

    return wrapper


def batch_insert(model_cls, data: Iterable[dict], batch_size=100) -> int:
    rows = 0
    inserts = []

    for item in data:
        inserts.append(item)
        rows += 1

        if rows % batch_size == 0:
            model_cls.insert_many(inserts).execute()
            inserts = []

    if inserts:
        model_cls.insert_many(inserts).execute()

    return rows


def crop_image_url(source_image, bounding_box) -> str:
    base_url = settings.OFF_IMAGE_BASE_URL + source_image
    y_min, x_min, y_max, x_max = bounding_box
    base_robotoff_url = settings.BaseURLProvider().robotoff().get()
    return f"{base_robotoff_url}/api/v1/images/crop?image_url={base_url}&y_min={y_min}&x_min={x_min}&y_max={y_max}&x_max={x_max}"


class BaseModel(peewee.Model):
    class Meta:
        database = db
        legacy_table_names = False

    def to_dict(self, **kwargs):
        return model_to_dict(self, **kwargs)


class ProductInsight(BaseModel):
    """Table to store the insights generated by Robotoff."""

    # ID is the unique ID for this insight.
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)

    # Barcode represents the barcode of the product for which the insight was generated.
    barcode = peewee.CharField(max_length=100, null=False, index=True)

    # Type represents the insight type - must match one of the types in robotoff.insights.dataclass.InsightType.
    type = peewee.CharField(max_length=256, index=True)

    # Contains some additional data based on the type of the insight from above.
    # NOTE: there is no 1:1 mapping between the type and the JSON format provided here, for example for
    # type==label, the data here could be: {"logo_id":X,"confidence":Y}, or {"text":X,"notify":Y}
    data = BinaryJSONField(index=True, default=dict)

    # Timestamp is the timestamp of when this insight was imported into the DB.
    timestamp = peewee.DateTimeField(null=True, index=True)

    # Stores the timestamp of when this insight was annotated, either by a human annotator or automatically.
    completed_at = peewee.DateTimeField(null=True)

    # The annotation of the given insight. Four possible values are possible:
    # null = This insight has not been annotated
    #  -1 = Rejected
    # 0 = 'I don't know'
    # 1 = Validated
    annotation = peewee.IntegerField(null=True, index=True)

    # Saves the value returned by Annotator.annotate
    # The value is mapped at `AnnotationStatus(enum)` class in annotate.py
    annotated_result = peewee.IntegerField(null=True, index=False)

    # The number of votes for this annotation.
    # Stored here for quick sorting.
    n_votes = peewee.IntegerField(null=False, index=True)

    # If the insight was annotated manually, this field stores the username of the annotator
    # (or first annotator, if multiple votes were cast).
    username = peewee.TextField(index=True, null=True)

    # Stores the list of counties that are associated with the product.
    # E.g. possible values are "en:united-states" or "en:france".
    countries = BinaryJSONField(null=True, index=True)

    # Stores the list of brands that are associated with the product.
    brands = BinaryJSONField(null=True, index=True)

    # Specifies the timestamp on an automatic_processing insight after which the insight should be applied.
    process_after = peewee.DateTimeField(null=True)

    # Value tag contains the normalized 'value' of the insight based on the OFF taxonomies.
    # Some insight types will populate both this field and the 'value' field below, some only this field.
    value_tag = peewee.TextField(null=True, index=True)

    # Value stores the value of the insight, for example the brand name for a product or the numeric value of the weight of the product.
    # Some insight types will populate both this field and the 'value_tag' field above, some only this field.
    # This field is set for the following insight types: brand, expiration_date, packager_code, packaging, product_weight and store.
    value = peewee.TextField(null=True, index=True)

    # If the insight was based on an image, this field points to that image.
    # The complete image path can be constructed with robotoff.settings.OFF_IMAGE_BASE_URL + source_image.
    source_image = peewee.TextField(null=True, index=True)

    # Automatic processing is set on insights where Robotoff deems the prediction to be valid, e.g. if the prediction is above a
    # pre-determined threshold.
    automatic_processing = peewee.BooleanField(default=False, index=True)

    server_domain = peewee.TextField(
        null=True, help_text="server domain linked to the insight", index=True
    )
    server_type = peewee.CharField(
        null=True,
        max_length=10,
        help_text="project associated with the server_domain, "
        "one of 'off', 'obf', 'opff', 'opf'",
        index=True,
    )

    # This field refers to the number of unique IPs that have scanned this product.
    unique_scans_n = peewee.IntegerField(default=0, index=True)

    # A reserved barcode is a barcode that is a 'per-weight' barcode.
    reserved_barcode = peewee.BooleanField(default=False, index=True)

    # Predictor stores what ML model/OCR processing generated this insight.
    predictor = peewee.CharField(max_length=100, null=True, index=True)

    # annotation campaigns enable contributors to focus their efforts (on
    # Hunger Games) on a subset of products. Each product have 0+ campaign
    # tags
    campaign = BinaryJSONField(null=True, index=True, default=list)


class Prediction(BaseModel):
    barcode = peewee.CharField(max_length=100, null=False, index=True)
    type = peewee.CharField(max_length=256, index=True)
    data = BinaryJSONField(index=True)
    timestamp = peewee.DateTimeField(index=True)
    value_tag = peewee.TextField(null=True)
    value = peewee.TextField(null=True)
    source_image = peewee.TextField(null=True, index=True)
    automatic_processing = peewee.BooleanField(null=True)
    server_domain = peewee.TextField(
        help_text="server domain linked to the insight", index=True
    )
    predictor = peewee.CharField(max_length=100, null=True)


class AnnotationVote(BaseModel):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    # The insight this vote belongs to.
    insight_id = peewee.ForeignKeyField(
        ProductInsight, null=False, backref="votes", on_delete="CASCADE"
    )
    # The username of the voter - if logged in.
    # Currently logged in users do not need to vote on an insight for their annotation to
    # be applied.
    username = peewee.TextField(index=True, null=True)
    # The value of the annotation, see ProductInsight.annotation.
    value = peewee.IntegerField(
        null=False, choices=[(-1, "False"), (0, "Unknown"), (1, "True")]
    )
    # If the request has a device_id, use that - otherwise use a secure hash of the IP address.
    device_id = peewee.TextField(index=True, null=False)
    # Creation date for bookkeeping.
    timestamp = peewee.DateTimeField(null=False, default=datetime.datetime.utcnow)


class ImageModel(BaseModel):
    barcode = peewee.CharField(max_length=100, null=False, index=True)
    uploaded_at = peewee.DateTimeField(null=True, index=True)
    image_id = peewee.CharField(max_length=50, null=False, index=True)
    # The complete image path can be constructed with robotoff.settings.OFF_IMAGE_BASE_URL + source_image.
    source_image = peewee.TextField(null=False, index=True)
    width = peewee.IntegerField(null=False, index=True)
    height = peewee.IntegerField(null=False, index=True)
    deleted = peewee.BooleanField(null=False, index=True, default=False)
    server_domain = peewee.TextField(null=True, index=True)
    server_type = peewee.CharField(null=True, max_length=10, index=True)

    class Meta:
        table_name = "image"


class ImagePrediction(BaseModel):
    """Table to store computer vision predictions (object detection,
    image segmentation,...) made by custom models.

    They are created by API `ImagePredictorResource`, `ImagePredictionImporterResource`
    or cli `import_logos`

    Predictions come from a model, see `ObjectDetectionModel` in
    robotoff/types.py for available models.
    """

    type = peewee.CharField(max_length=256)
    model_name = peewee.CharField(max_length=100, null=False, index=True)
    model_version = peewee.CharField(max_length=256, null=False, index=True)
    data = BinaryJSONField(index=True)
    timestamp = peewee.DateTimeField(null=True)
    image = peewee.ForeignKeyField(ImageModel, null=False, backref="predictions")
    max_confidence = peewee.FloatField(
        null=True,
        index=True,
        help_text="for object detection models, confidence of the highest confident"
        "object detected, null if no object was detected",
    )


class LogoAnnotation(BaseModel):
    """Annotation(s) for an image prediction
    (an image prediction might lead to several annotations)

    At the moment, this is mostly for logo (see run_logo_object_detection),
    when we have a logo prediction above a certain threshold we create an entry,
    to ask user for annotation on the logo (https://hunger.openfoodfacts.org/logos)
    and eventual annotation will land there.
    """

    image_prediction = peewee.ForeignKeyField(
        ImagePrediction, null=False, backref="logos"
    )
    index = peewee.IntegerField(null=False, constraints=[peewee.Check("index >= 0")])
    bounding_box = BinaryJSONField(null=False)
    score = peewee.FloatField(null=False)
    annotation_value = peewee.CharField(null=True, index=True)
    annotation_value_tag = peewee.CharField(null=True, index=True)
    taxonomy_value = peewee.CharField(null=True, index=True)
    annotation_type = peewee.CharField(
        null=True,
        index=True,
        help_text="Category of the annotation. Current possible values: brand, "
        "category, label, no_logo, nutrition_label, packager_code, packaging, "
        "qr_code, store",
    )
    username = peewee.TextField(null=True, index=True)
    completed_at = peewee.DateTimeField(null=True, index=True)
    nearest_neighbors = BinaryJSONField(null=True)

    class Meta:
        constraints = [peewee.SQL("UNIQUE(image_prediction_id, index)")]

    def get_crop_image_url(self) -> str:
        return crop_image_url(
            self.image_prediction.image.source_image, self.bounding_box
        )


class LogoEmbedding(BaseModel):
    logo = peewee.ForeignKeyField(
        LogoAnnotation,
        null=False,
        backref="embeddings",
        on_delete="CASCADE",
        unique=True,
        primary_key=True,
    )
    embedding = peewee.BlobField(null=False)

    class Meta:
        schema = "embedding"


class LogoConfidenceThreshold(BaseModel):
    type = peewee.CharField(null=True, index=True)
    value = peewee.CharField(null=True, index=True)
    threshold = peewee.FloatField(null=False)


MODELS = [
    Prediction,
    ProductInsight,
    ImageModel,
    ImagePrediction,
    LogoAnnotation,
    LogoEmbedding,
    LogoConfidenceThreshold,
    AnnotationVote,
]
