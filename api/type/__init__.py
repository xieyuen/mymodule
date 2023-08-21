from ...type.base import \
	isInteger, isFloat, isComplex, isString, \
	isList, isTuple, isDict, isSet, \
	isCallable, isIterable, isIterator, \
	isGenerater, isBool, isNone

from ...type.cname import isInt, isStr, isNum

from ...type.extra import \
	isLongReal, isReal, isNumber, isEmpty, isNumNoBool, \
	isCanFor, isImmutable


__all__ = [
	# -------------------
	#    Base Function
	# -------------------

	'isInteger', 'isFloat', 'isComplex', 'isString',
	'isList', 'isTuple', 'isDict', 'isSet', 'isBool',
	'isCallable', 'isIterable', 'isIterator', 'isGenerater',
	'isNone',

	# --------------------
	#    Extra Function
	# --------------------

	'isLongReal', 'isReal', 'isNumber',
	'isEmpty', 'isNumNoBool', 'isCanFor',
	'isImmutable',

	# --------------------
	#    Canonical Name
	# --------------------

	'isInt', 'isStr', 'isNum',
]