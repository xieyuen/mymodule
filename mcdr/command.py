'''
MCDR 指令编辑包
`from mymodule.mcdr.command import *`就行了
'''


# Command Arguments
from mcdreforged.command.builder.nodes.arguments import \
	Number, Integer, Float, Text, QuotableText, \
	GreedyText, Boolean, Enumeration
from mcdreforged.command.builder.nodes.basic import AbstractNode, Literal, ArgumentNode

# PLugin Server Interface
from mcdreforged.api.types import ServerInterface, PluginServerInterface

# Simple Command Builder
from mcdreforged.api.command import SimpleCommandBuilder
SCB = builder = SimpleCommandBuilder()

# Exceptions
from mcdreforged.command.builder.exception import \
	LiteralNotMatch, NumberOutOfRange, IllegalArgument, EmptyText, \
	UnknownCommand, UnknownArgument, CommandSyntaxError, UnknownRootArgument, \
	RequirementNotMet, IllegalNodeOperation, CommandError, InvalidNumber, \
	InvalidInteger, InvalidFloat, UnclosedQuotedString, IllegalEscapesUsage, InvalidBoolean, \
	InvalidEnumeration, TextLengthOutOfRange, CommandErrorBase, AbstractOutOfRange

# Plugin things
from mcdreforged.plugin.meta.metadata import Metadata
from mcdreforged.plugin.meta.version import Version, VersionRequirement

# Info
from mcdreforged.info_reactor.info import Info
from mcdreforged.info_reactor.server_information import ServerInformation

# Permission
from mcdreforged.permission.permission_level import PermissionLevel

# Command sources
from mcdreforged.command.command_source import \
	CommandSource, ConsoleCommandSource, PlayerCommandSource, \
	InfoCommandSource, PluginCommandSource

# Loggers
from mcdreforged.utils.logger import SyncStdoutStreamHandler, MCDReforgedLogger
