"""
MCDR 指令编辑包
`from mymodule.mcdr.command import *`就行了
"""

# Simple Command Builder
from mcdreforged.api.command import SimpleCommandBuilder
# Plugin Server Interface
from mcdreforged.api.types import ServerInterface, PluginServerInterface
# Exceptions
from mcdreforged.command.builder.exception import \
    LiteralNotMatch, NumberOutOfRange, IllegalArgument, EmptyText, \
    UnknownCommand, UnknownArgument, CommandSyntaxError, UnknownRootArgument, \
    RequirementNotMet, IllegalNodeOperation, CommandError, InvalidNumber, \
    InvalidInteger, InvalidFloat, UnclosedQuotedString, IllegalEscapesUsage, InvalidBoolean, \
    InvalidEnumeration, TextLengthOutOfRange, CommandErrorBase, AbstractOutOfRange
# Command Arguments
from mcdreforged.command.builder.nodes.arguments import \
    Number, Integer, Float, Text, QuotableText, \
    GreedyText, Boolean, Enumeration
from mcdreforged.command.builder.nodes.basic import \
    AbstractNode, Literal, ArgumentNode
# Command sources
from mcdreforged.command.command_source import \
    CommandSource, ConsoleCommandSource, PlayerCommandSource, \
    InfoCommandSource, PluginCommandSource
# Info
from mcdreforged.info_reactor.info import Info
from mcdreforged.info_reactor.server_information import ServerInformation
# Permission
from mcdreforged.permission.permission_level import PermissionLevel
# Plugin things
from mcdreforged.plugin.meta.metadata import Metadata
from mcdreforged.plugin.meta.version import Version, VersionRequirement
# Loggers
from mcdreforged.utils.logger import SyncStdoutStreamHandler, MCDReforgedLogger

SCBInstance = builder = SimpleCommandBuilder()


class CommandNodes:
    Number = Number
    Integer = Integer
    Float = Float
    Text = Text
    Enumeration = Enumeration
    QuotableText = QuotableText
    AbstractNode = AbstractNode
    GreedyText = GreedyText
    Literal = Literal
    Boolean = Boolean
    ArgumentNode = ArgumentNode


class MCDReforgedExceptions:
    LiteralNotMatch = LiteralNotMatch
    UnclosedQuotedString = UnclosedQuotedString
    NumberOutOfRange = NumberOutOfRange
    IllegalEscapesUsage = IllegalEscapesUsage
    IllegalArgument = IllegalArgument
    InvalidBoolean = InvalidBoolean
    EmptyText = EmptyText
    InvalidEnumeration = InvalidEnumeration
    UnknownCommand = UnknownCommand
    TextLengthOutOfRange = TextLengthOutOfRange
    UnknownArgument = UnknownArgument
    CommandErrorBase = CommandErrorBase
    CommandSyntaxError = CommandSyntaxError
    AbstractOutOfRange = AbstractOutOfRange
    UnknownRootArgument = UnknownRootArgument
    InvalidNumber = InvalidNumber
    RequirementNotMet = RequirementNotMet
    InvalidInteger = InvalidInteger
    IllegalNodeOperation = IllegalNodeOperation
    InvalidFloat = InvalidFloat
    CommandError = CommandError


class PluginUtils:
    PluginServerInterface = PluginServerInterface
    Exceptions = MCDReforgedExceptions
    Nodes = CommandNodes


__all__ = [
    # -------------------------
    #     Command Arguments
    # -------------------------

    'Number', 'Integer', 'Float',
    'Text', 'Enumeration',
    'QuotableText', 'AbstractNode',
    'GreedyText', 'Literal',
    'Boolean', 'ArgumentNode',

    # -------------------------
    #     Server Interface
    # -------------------------

    'ServerInterface', 'PluginServerInterface',

    # -------------------------
    #     Command Builder
    # -------------------------

    'SimpleCommandBuilder', 'SCBInstance', 'builder',

    # --------------------------
    #   MCDReforged Exceptions
    # --------------------------

    'LiteralNotMatch', 'UnclosedQuotedString',
    'NumberOutOfRange', 'IllegalEscapesUsage',
    'IllegalArgument', 'InvalidBoolean',
    'EmptyText', 'InvalidEnumeration',
    'UnknownCommand', 'TextLengthOutOfRange',
    'UnknownArgument', 'CommandErrorBase',
    'CommandSyntaxError', 'AbstractOutOfRange',
    'UnknownRootArgument', 'InvalidNumber',
    'RequirementNotMet', 'InvalidInteger',
    'IllegalNodeOperation', 'InvalidFloat',
    'CommandError',

    # -------------------------
    #       Plugin Things
    # -------------------------

    'Metadata',
    'Version',
    'VersionRequirement',

    # -------------------------
    #        Server Info
    # -------------------------

    'Info', 'ServerInformation',

    # -------------------------
    #     Permission Level
    # -------------------------

    'PermissionLevel',

    # ------------------------
    #      Command Source
    # ------------------------

    'CommandSource', 'InfoCommandSource',
    'ConsoleCommandSource', 'PluginCommandSource',
    'PlayerCommandSource',

    # ------------------------
    #    MCDReforged Logger
    # ------------------------
    'SyncStdoutStreamHandler',
    'MCDReforgedLogger',

    # --------------------
    #      some tools
    # --------------------
    'CommandNodes', 'MCDReforgedExceptions',
]
