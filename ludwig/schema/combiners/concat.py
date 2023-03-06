from typing import Any, Dict, List, Optional, Union

from ludwig.api_annotations import DeveloperAPI
from ludwig.schema import common_fields
from ludwig.schema import utils as schema_utils
from ludwig.schema.combiners.base import BaseCombinerConfig
from ludwig.schema.metadata import COMBINER_METADATA, COMMON_METADATA
from ludwig.schema.utils import ludwig_dataclass


@DeveloperAPI
@ludwig_dataclass
class ConcatCombinerConfig(BaseCombinerConfig):
    """Parameters for concat combiner."""

    @staticmethod
    def module_name():
        return "ConcatCombiner"

    type: str = schema_utils.ProtectedString(
        "concat",
        description=COMBINER_METADATA["ConcatCombiner"]["type"].long_description,
    )

    dropout: float = common_fields.DropoutField()

    activation: str = schema_utils.ActivationOptions(default="relu")

    flatten_inputs: bool = schema_utils.Boolean(
        default=False,
        description="Whether to flatten input tensors to a vector.",
        parameter_metadata=COMBINER_METADATA["ConcatCombiner"]["flatten_inputs"],
    )

    residual: bool = common_fields.ResidualField()

    use_bias: bool = schema_utils.Boolean(
        default=True,
        description="Whether the layer uses a bias vector.",
        parameter_metadata=COMBINER_METADATA["ConcatCombiner"]["use_bias"],
    )

    bias_initializer: Union[str, Dict] = schema_utils.InitializerOrDict(
        default="zeros",
        description="Initializer to use for the bias vector.",
        parameter_metadata=COMMON_METADATA["bias_initializer"],
    )

    weights_initializer: Union[str, Dict] = schema_utils.InitializerOrDict(
        default="xavier_uniform",
        description="Initializer to use for the weights matrix.",
        parameter_metadata=COMMON_METADATA["weights_initializer"],
    )

    num_fc_layers: int = common_fields.NumFCLayersField()

    output_size: int = schema_utils.PositiveInteger(
        default=256,
        description="Output size of a fully connected layer.",
        parameter_metadata=COMBINER_METADATA["ConcatCombiner"]["output_size"],
    )

    norm: Optional[str] = common_fields.NormField()

    norm_params: Optional[dict] = common_fields.NormParamsField()

    fc_layers: Optional[List[Dict[str, Any]]] = common_fields.FCLayersField()
