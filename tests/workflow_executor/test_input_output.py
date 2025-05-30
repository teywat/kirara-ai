from kirara_ai.workflow.core.block.input_output import Input, Output


def test_input_validation():
    """Test input validation."""
    input_obj = Input(
        name="input1", label="输入1", data_type=int, description="An integer input"
    )
    assert input_obj.validate(10) is True
    assert input_obj.validate("10") is False
    assert input_obj.validate(None) is False  # Not nullable by default

    nullable_input = Input(
        name="input2",
        label="输入2",
        data_type=int,
        description="A nullable integer input",
        nullable=True,
    )
    assert nullable_input.validate(None) is True


def test_output_validation():
    """Test output validation."""
    output_obj = Output(
        name="output1", label="输出1", data_type=str, description="A string output"
    )
    assert output_obj.validate("test") is True
    assert output_obj.validate(10) is False
