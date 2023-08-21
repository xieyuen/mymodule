from ...type.base import \
	isInteger, isFloat, isComplex, isString, \
	isList, isTuple, isDict, isSet, \
	isCallable, isIterable, isIterator, \
	isGenerator, isBool, isNone

from ...type.cname import \
	isInt, isStr, isNum, isDictionary, \
	isChar, isMap, isBoolean

from ...type.extra import \
	isLongReal, isReal, isNumber, isEmpty, isNumNoBool, \
	isCanFor, isImmutable, isCharacter, isArray, isDouble


__all__ = [
	# -------------------
	#    Base Function
	# -------------------

	'isInteger', 'isFloat', 'isComplex', 'isString',
	'isList', 'isTuple', 'isDict', 'isSet', 'isBool',
	'isCallable', 'isIterable', 'isIterator', 'isGenerator',
	'isNone',

	# --------------------
	#    Extra Function
	# --------------------

	'isLongReal', 'isReal', 'isNumber',
	'isEmpty', 'isNumNoBool', 'isCanFor',
	'isImmutable', 'isCharacter', 'isArray',
	'isDouble',

	# --------------------
	#    Canonical Name
	# --------------------

	'isInt', 'isStr', 'isNum', 'isDictionary', 'isChar',
	'isMap', 'isBoolean',
]
