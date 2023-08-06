from relevanceai.operations_new.emotion.transform import EmotionTransform
from relevanceai.operations_new.ops_base import OperationAPIBase


class EmotionOps(OperationAPIBase, EmotionTransform):
    """
    Add emotions
    """

    def __init__(
        self,
        text_fields: list,
        model_name="joeddav/distilbert-base-uncased-go-emotions-student",
        output_fields: list = None,
        min_score: float = 0.3,
        **kwargs,
    ):
        self.model_name = model_name
        self.text_fields = text_fields
        if output_fields is not None:
            self.output_fields = output_fields
        else:
            self.output_fields = [self._generate_output_field(t) for t in text_fields]
        self.min_score = min_score
        super().__init__(**kwargs)

    @property
    def name(self):
        return "emotion"
