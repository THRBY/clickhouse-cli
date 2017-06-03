from clickhouse_cli.clickhouse.sqlparse_patch import KEYWORDS as sqlparse_keywords

FUNCTIONS = (
    # arithmetic / logic
    'plus',
    'minus',
    'multiply',
    'divide',
    'intDiv',
    'intDivOrZero',
    'modulo',
    'negate',
    'abs',
    'bitAnd',
    'bitOr',
    'bitXor',
    'bitNot',
    'bitShiftLeft',
    'bitShiftRight',
    'equals',
    'notEquals',
    'less',
    'greater',
    'lessOrEquals',
    'greaterOrEquals',
    'and',
    'or',
    'not',
    'xor',

    # type conversion
    'toUInt8',
    'toUInt16',
    'toUInt32',
    'toUInt64',
    'toInt8',
    'toInt16',
    'toInt32',
    'toInt64',
    'toFloat32',
    'toFloat64',
    'toDate',
    'toDateTime',
    'toString',
    'toFixedString',
    'toStringCutToZero',

    'toUInt8OrZero',
    'toUInt16OrZero',
    'toUInt32OrZero',
    'toUInt64OrZero',
    'toInt8OrZero',
    'toInt16OrZero',
    'toInt32OrZero',
    'toInt64OrZero',
    'toFloat32OrZero',
    'toFloat64OrZero'

    'reinterpretAsUInt8',
    'reinterpretAsUInt16',
    'reinterpretAsUInt32',
    'reinterpretAsUInt64',
    'reinterpretAsInt8',
    'reinterpretAsInt16',
    'reinterpretAsInt32',
    'reinterpretAsInt64',
    'reinterpretAsFloat32',
    'reinterpretAsFloat64',
    'reinterpretAsDate',
    'reinterpretAsDateTime',
    'reinterpretAsString',

    # date/time

    'toYear',
    'toMonth',
    'toDayOfMonth',
    'toDayOfWeek',
    'toHour',
    'toMinute',
    'toSecond',
    'toMonday',
    'toStartOfMonth',
    'toStartOfQuarter',
    'toStartOfYear',
    'toStartOfMinute',
    'toStartOfFiveMinute',
    'toStartOfHour',
    'toTime',
    'toRelativeYearNum',
    'toRelativeMonthNum',
    'toRelativeWeekNum',
    'toRelativeDayNum',
    'toRelativeHourNum',
    'toRelativeMinuteNum',
    'toRelativeSecondNum',
    'now',
    'today',
    'yesterday',
    'timeSlot',
    'timeSlots',

    # string
    'empty',
    'notEmpty',
    'length',
    'lengthUTF8',
    'lower',
    'upper',
    'lowerUTF8',
    'upperUTF8',
    'reverse',
    'reverseUTF8',
    'concat',
    'substring',
    'substringUTF8',
    'appendTrailingCharIfAbsent',
    'convertCharset',

    # string find
    'position',
    'positionUTF8',
    'positionCaseInsensitive',
    'positionCaseInsensitiveUTF8',
    'match',
    'extract',
    'extractAll',
    'like',
    'notLike',

    # string find & replace
    'replaceOne',
    'replaceAll',
    'replaceRegexpOne',
    'replaceRegexpAll',

    # array
    'empty',
    'notEmpty',
    'length',
    'emptyArrayUInt8',
    'emptyArrayUInt16',
    'emptyArrayUInt32',
    'emptyArrayUInt64',
    'emptyArrayInt8',
    'emptyArrayInt16',
    'emptyArrayInt32',
    'emptyArrayInt64',
    'emptyArrayFloat32',
    'emptyArrayFloat64',
    'emptyArrayDate',
    'emptyArrayDateTime',
    'emptyArrayString',
    'range',
    'array',
    'arrayElement',
    'has',
    'indexOf',
    'countEqual',
    'arrayEnumerate',
    'arrayEnumerateUniq',
    'arrayJoin',

    # higher-level
    'lambda',
    'arrayMap',
    'arrayFilter',
    'arrayCount',
    'arrayExists',
    'arrayAll',
    'arraySum',
    'arrayFirst',
    'arrayFirstIndex',

    # array / string
    'splitByChar',
    'splitByString',
    'arrayStringConcat',
    'alphaTokens',

    # URL
    'protocol',
    'domain',
    'domainWithoutWWW',
    'topLevelDomain',
    'firstSignificantSubdomain',
    'cutToFirstSignificantSubdomain',
    'path',
    'pathFull',
    'queryString',
    'fragment',
    'queryStringAndFragment',
    'extractURLParameter',
    'extractURLParameters',
    'extractURLParameterNames',
    'URLHierarchy',
    'URLPathHierarchy',
    'cutWWW',
    'cutQueryString',
    'cutFragment',
    'cutQueryStringAndFragment',
    'cutURLParameter',

    # IP
    'IPv4NumToString',
    'IPv4StringToNum',
    'IPv4NumToStringClassC',
    'IPv6NumToString',
    'IPv6StringToNum',

    # PRNG
    'rand',
    'rand64',

    # hash
    'halfMD5',
    'MD5',
    'sipHash64',
    'sipHash128',
    'cityHash64',
    'intHash32',
    'intHash64',
    'SHA1',
    'SHA224',
    'SHA256',
    'URLHash',

    # encode / decode
    'hex',
    'unhex',
    'bitmaskToList',
    'bitmaskToArray',

    # rounding
    'floor',
    'ceil',
    'round',
    'roundToExp2',
    'roundDuration',
    'roundAge',

    # conditional
    'if',
    'multiIf',

    # math
    'e',
    'pi',
    'exp',
    'log',
    'exp2',
    'log2',
    'exp10',
    'log10',
    'sqrt',
    'cbrt',
    'erf',
    'erfc',
    'lgamma',
    'tgamma',
    'sin',
    'cos',
    'tan',
    'asin',
    'acos',
    'atan',
    'pow',

    # metrika dictionaries
    'regionToCity',
    'regionToArea',
    'regionToDistrict',
    'regionToCountry',
    'regionToContinent',
    'regionToTopContinent',
    'regionToPopulation',
    'regionIn',
    'regionHierarchy',
    'regionToName',
    'OSToRoot',
    'OSIn',
    'OSHierarchy',
    'SEToRoot',
    'SEIn',
    'SEHierarchy',

    # external dictionaries
    'dictGetUInt8',
    'dictGetUInt16',
    'dictGetUInt32',
    'dictGetUInt64',
    'dictGetInt8',
    'dictGetInt16',
    'dictGetInt32',
    'dictGetInt64',
    'dictGetFloat32',
    'dictGetFloat64',
    'dictGetDate',
    'dictGetDateTime',
    'dictGetString',
    'dictGetTOrDefault',
    'dictIsIn',
    'dictGetHierarchy',
    'dictHas',

    # json
    'visitParamHas',
    'visitParamExtractUInt',
    'visitParamExtractInt',
    'visitParamExtractFloat',
    'visitParamExtractBool',
    'visitParamExtractRaw',
    'visitParamExtractString',

    # IN support
    'in',
    'notIn',
    'globalIn',
    'globalNotIn',
    'tuple',
    'tupleElement',

    # misc
    'hostName',
    'visibleWidth',
    'toTypeName',
    'blockSize',
    'materialize',
    'ignore',
    'sleep',
    'currentDatabase',
    'isFinite',
    'isInfinite',
    'isNaN',
    'hasColumnInTable',
    'bar',
    'transform',
    'runningAccumulate',
    'runningDifference',
    'rowNumberInAllBlocks',
    'uptime',
    'version',
    'least',
    'greatest',
    'formatReadableSize',

    'arrayJoin',
)

CASE_INSENSITIVE_FUNCTIONS = (
    'COUNT',

    'CORR',
    'VAR_SAMP',
    'VAR_POP',
    'STDDEV_SAMP',
    'STDDEV_POP',
    'COVAR_SAMP',
    'COVAR_POP',

    'AVG',
    'SUM',
    'MIN',
    'MAX',
)

AGGREGATION_FUNCTIONS_BASE = (
    'count',
    'any',
    'anyLast',
    'min',
    'max',
    'argMin',
    'argMax',
    'sum',
    'avg',
    'uniq',
    'uniqCombined',
    'uniqHLL12',
    'uniqExact',
    'groupArray',
    'groupUniqArray',
    'quantile',
    'quantileDeterministic',
    'quantileTiming',
    'quantileTimingWeighted',
    'quantileExact',
    'quantileExactWeighted',
    'quantileTDigest',
    'median',
    'quantiles',
    'varSamp',
    'varPop',
    'stddevSamp',
    'stddevPop',
    'covarSamp',
    'covarPop',
    'corr',
    'sequenceMatch',
    'sequenceCount',
    'uniqUpTo',
    'topK',
)

AGGREGATION_FUNCTIONS = (
    AGGREGATION_FUNCTIONS_BASE +
    tuple(name + 'If' for name in AGGREGATION_FUNCTIONS_BASE) +
    tuple(name + 'Array' for name in AGGREGATION_FUNCTIONS_BASE) +
    tuple(name + 'Merge' for name in AGGREGATION_FUNCTIONS_BASE) +
    tuple(name + 'State' for name in AGGREGATION_FUNCTIONS_BASE) +
    tuple(name + 'MergeState' for name in AGGREGATION_FUNCTIONS_BASE)
)

DATATYPES = (
    'UInt8',
    'UInt16',
    'UInt32',
    'UInt64',
    'Int8',
    'Int16',
    'Int32',
    'Int64',
    'Float32',
    'Float64',
    'String',
    'FixedString',
    'Date',
    'DateTime',
    'Enum',
    'Array',
    'Tuple',
    'Nested',
)

OPERATORS = (
    'LIKE',
    'NOT LIKE',
    'IN',
    'NOT IN',
    'GLOBAL IN',
    'GLOBAL NOT IN',
    'AND',
    'OR',
    'NOT',
    'BETWEEN',
)

PRETTY_FORMATS = (
    'Pretty',
    'PrettyCompact',
    'PrettyCompactMonoBlock',
    'PrettySpace',
    'PrettyNoEscapes',
    'PrettyCompactNoEscapes',
    'PrettySpaceNoEscapes',
)

FORMATS = PRETTY_FORMATS + (
    'Native',
    'TabSeparated',
    'TabSeparatedWithNames',
    'TabSeparatedWithNamesAndTypes',
    'TabSeparatedRaw',
    'TSV',
    'TSVWithNames',
    'TSVWithNamesAndTypes',
    'TSVRaw',
    'BlockTabSeparated',
    'CSV',
    'CSVWithNames',
    'RowBinary',
    'Vertical',
    'Values',
    'JSON',
    'JSONCompact',
    'JSONEachRow',
    'TSKV',
    'XML',
    'Null',
    'Dictionary',
)

READ_QUERIES = (
    'SELECT',
    'SHOW',
    'DESC',
    'DESCRIBE',
    'USE',
    'EXISTS',
)

WRITE_QUERIES = (
    'INSERT',
    'CREATE',
    'ATTACH',
    'DETACH',
    'DROP',
    'RENAME',
    'ALTER',
    'SET',
    'OPTIMIZE',
)

FORMATTABLE_QUERIES = (
    'INSERT',
    'SELECT',
    'SHOW',
    'DESC',
    'DESCRIBE',
    'EXISTS',
)

KEYWORDS = tuple(sqlparse_keywords.keys())

EXIT_COMMANDS = (
    'exit',
    'quit',
    'logout',
    'учше',
    'йгше',
    'дщпщге',
    'exit;',
    'quit;',
    'logout;',
    'учшеж',
    'йгшеж',
    'дщпщгеж',
    'q',
    'й',
    r'\q',
    r'\Q',
    ':q',
    r'\й',
    r'\Й',
    'Жй',
)

CREATE_SUBCOMMANDS = (
    'DATABASE',
    'TABLE',
    'VIEW',
)

DROP_SUBCOMMANDS = (
    'DATABASE',
    'TABLE'
)

SHOW_SUBCOMMANDS = (
    'DATABASES',
    'TABLES',
    'PROCESSLIST',
    'CREATE TABLE',
)

HELP_COMMANDS = (
    'help',
    r'\?',
)

REDIRECTION_COMMANDS = (
    r'\d',
    r'\d+',
    r'\dt',
    r'\c',
    r'\l',
    r'\ps',
    r'\kill',
)

INTERNAL_COMMANDS = EXIT_COMMANDS + HELP_COMMANDS + REDIRECTION_COMMANDS
