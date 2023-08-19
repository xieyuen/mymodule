from ...type.base import \
	isInteger, isFloat, isComplex, isString, \
	isList, isTuple, isDict, isSet, \
	isCallable, isIterable, isIterator, \
	isGenerater, isBool, isNone

from ...type.cname import isInt, isStr, isNum

from ...type.extra import \
	isLongReal, isReal, isNumber, isEmpty, isNumNoBool, \
	isCanFor


__all__ = [
	# -------------------
	#    Base Function
	# -------------------

	'isInteger', 'isFloat', 'isComplex', 'isString',
	'isList', 'isTuple', 'isDict', 'isSet',
	'isCallable', 'isIterable', 'isIterator', 'isGenerater',
	'isBool', 'isNone',

	# --------------------
	#    Extra Function
	# --------------------

	'isLongReal', 'isReal', 'isNumber',
	'isEmpty', 'isNumNoBool', 'isCanFor',

	# --------------------
	#    Canonical Name
	# --------------------

	'isInt', 'isStr', 'isNum',
]