from __future__ import annotations

from typing import Annotated, Optional

from pydantic import BaseModel, Field


class NameLeaf(BaseModel):
    __root__: str
    """
    Interface name. Example value: GigabitEthernet 0/0/0
    """


class AddressLeaf(BaseModel):
    __root__: str
    """
    Interface IP address. Example value: 10.10.10.1
    """


class PortLeaf(BaseModel):
    __root__: Annotated[int, Field(ge=0, le=65535)]
    """
    Port number. Example value: 8080
    """


class InterfacesContainer(BaseModel):
    """
    Just a simple example of a container.
    """

    name: Annotated[NameLeaf, Field(alias='interfaces:name')]
    """
    Interface name. Example value: GigabitEthernet 0/0/0
    """
    address: Annotated[AddressLeaf, Field(alias='interfaces:address')]
    """
    Interface IP address. Example value: 10.10.10.1
    """
    port: Annotated[PortLeaf, Field(alias='interfaces:port')]
    """
    Port number. Example value: 8080
    """


class Model(BaseModel):
    """
    Initialize an instance of this class and serialize it to JSON; this results in a RESTCONF payload.

    ## Tips
    Initialization:
    - all values have to be set via keyword arguments
    - if a class contains only a `__root__` field, it can be initialized as follows:
        - `member=MyNode(__root__=<value>)`
        - `member=<value>`

    Serialziation:
    - `exclude_defaults=True` omits fields set to their default value (recommended)
    - `by_alias=True` ensures qualified names are used (necessary)
    """

    interfaces: Annotated[
        Optional[InterfacesContainer], Field(alias='interfaces:interfaces')
    ] = None


from pydantic import BaseConfig, Extra

BaseConfig.allow_population_by_field_name = True
BaseConfig.smart_union = True  # See Pydantic issue#2135 / pull#2092
BaseConfig.extra = Extra.forbid


if __name__ == "__main__":
    # Demonstration purposes only. Not included in actual output.
    # To run: pdm run python out/out.py
    from pathlib import Path

    with open(Path(__file__).parent.joinpath("sample_data.json")) as fd:
        import json

        input = json.load(fd)
        print(f"{input=}")
        model = Model(**input)
        print("Instantiation successful!")

        output = model.json(exclude_defaults=True, by_alias=True)
        print(f"{output=}")

        assert json.loads(output) == input
        print("Serialization successful!")
