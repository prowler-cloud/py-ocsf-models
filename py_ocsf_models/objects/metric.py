from pydantic.v1 import BaseModel


class Metric(BaseModel):
    """
    The Metric object defines a simple name/value pair entity for a metric.
    """

    name: str
    value: str
