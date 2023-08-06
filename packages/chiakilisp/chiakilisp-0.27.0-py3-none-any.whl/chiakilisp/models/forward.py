# pylint: disable=arguments-renamed
# pylint: disable=too-few-public-methods

"""Forward declaration of some models"""

from chiakilisp.models.token import Token


class CommonType:

    """Forward declaration for both models"""

    _properties: dict

    def wrapped(self) -> str:

        """Just to define 'wrapped()' method signature"""

    def dump(self, indent: int) -> None:

        """Just to define 'dump()' method signature"""

    def execute(self, env: dict, top: bool):

        """Just to define 'execute()' method signature"""

    def set_properties(self, properties: list) -> None:

        """Assigns a list of properties as a dict"""

        self._properties = dict(
            map(lambda prop: prop.split(':'),
                properties)
        )

    def property(self, name: str, default=None) -> str:

        """Returns property (default) value by name"""

        return self._properties.get(name, default)

    def properties(self) -> dict:

        """Returns properties"""

        return self._properties

    def prefix(self) -> str:

        """Returns prefix according to prop"""

        if self.property('quoted') == 'single':
            return "'"
        if self.property('quoted') == 'apostrophe':
            return '`'

        return ''


class LiteralType(CommonType):

    """Forward declaration for Literal model"""

    def token(self) -> Token:

        """Just to define 'token()' method signature"""


class ExpressionType(CommonType):

    """Forward declaration for Expression model"""

    def children(self) -> list:

        """Just to define 'children()' method signature"""
