define("ace/mode/perl6_highlight_rules",["require","exports","module","ace/lib/oop","ace/mode/text_highlight_rules"], function(require, exports, module) {
"use strict";

var oop = require("../lib/oop");
var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;

var Perl6HighlightRules = function() {

    var keywords = (
        "my|our|class|role|grammar|is|does|sub|method|submethod|try|" +
        "default|when|if|elsif|else|unless|with|orwith|without|for|given|proceed|" +
        "succeed|loop|while|until|repeat|module|use|need|import|require|unit|" +
        "constant|enum|multi|return|has|token|rule|make|made|proto|state|augment|" +
        "but|anon|supersede|let|subset|gather|returns|return-rw|temp|" +
        "BEGIN|CHECK|INIT|END|CLOSE|ENTER|LEAVE|KEEP|UNDO|PRE|POST|FIRST|NEXT|LAST|CATCH|CONTROL|QUIT|DOC"
    );

    var types = (
        "Any|Array|Associative|AST|atomicint|Attribute|Backtrace|Backtrace::Frame|" +
        "Bag|Baggy|BagHash|Blob|Block|Bool|Buf|Callable|CallFrame|Cancellation|" +
        "Capture|Channel|Code|compiler|Complex|ComplexStr|Cool|CurrentThreadScheduler|" +
        "Cursor|Date|Dateish|DateTime|Distro|Duration|Encoding|Exception|Failure|"+
        "FatRat|Grammar|Hash|HyperWhatever|Instant|Int|IntStr|IO|IO::ArgFiles|"+
        "IO::CatHandle|IO::Handle|IO::Notification|IO::Path|IO::Path::Cygwin|"+
        "IO::Path::QNX|IO::Path::Unix|IO::Path::Win32|IO::Pipe|IO::Socket|"+
        "IO::Socket::Async|IO::Socket::INET|IO::Spec|IO::Spec::Cygwin|IO::Spec::QNX|"+
        "IO::Spec::Unix|IO::Spec::Win32|IO::Special|Iterable|Iterator|Junction|Kernel|"+
        "Label|List|Lock|Lock::Async|Macro|Map|Match|Metamodel::AttributeContainer|"+
        "Metamodel::C3MRO|Metamodel::ClassHOW|Metamodel::EnumHOW|Metamodel::Finalization|"+
        "Metamodel::MethodContainer|Metamodel::MROBasedMethodDispatch|Metamodel::MultipleInheritance|"+
        "Metamodel::Naming|Metamodel::Primitives|Metamodel::PrivateMethodContainer|"+
        "Metamodel::RoleContainer|Metamodel::Trusting|Method|Mix|MixHash|Mixy|Mu|"+
        "NFC|NFD|NFKC|NFKD|Nil|Num|Numeric|NumStr|ObjAt|Order|Pair|Parameter|Perl|"+
        "Pod::Block|Pod::Block::Code|Pod::Block::Comment|Pod::Block::Declarator|"+
        "Pod::Block::Named|Pod::Block::Para|Pod::Block::Table|Pod::Heading|Pod::Item|"+
        "Positional|PositionalBindFailover|Proc|Proc::Async|Promise|Proxy|PseudoStash|"+
        "QuantHash|Range|Rat|Rational|RatStr|Real|Regex|Routine|Scalar|Scheduler|"+
        "Semaphore|Seq|Set|SetHash|Setty|Signature|Slip|Stash|Str|StrDistance|Stringy|"+
        "Sub|Submethod|Supplier|Supplier::Preserving|Supply|Systemic|Tap|Telemetry|"+
        "Telemetry::Instrument::Thread|Telemetry::Instrument::Usage|Telemetry::Period|"+
        "Telemetry::Sampler|Thread|ThreadPoolScheduler|UInt|Uni|utf8|Variable|Version|"+
        "VM|Whatever|WhateverCode|WrapHandle|int|uint|num|str|"+
        "int8|int16|int32|int64|uint8|uint16|uint32|uint64|long|longlong|num32|num64|size_t|bool|CArray|Pointer|"+
		"Backtrace|Backtrace::Frame|Exception|Failure|X::AdHoc|X::Anon::Augment|X::Anon::Multi|"+
		"X::Assignment::RO|X::Attribute::NoPackage|X::Attribute::Package|X::Attribute::Undeclared|"+
		"X::Augment::NoSuchType|X::Bind|X::Bind::NativeType|X::Bind::Slice|X::Caller::NotDynamic|"+
		"X::Channel::ReceiveOnClosed|X::Channel::SendOnClosed|X::Comp|X::Composition::NotComposable|"+
		"X::Constructor::Positional|X::ControlFlow|X::ControlFlow::Return|X::DateTime::TimezoneClash|"+
		"X::Declaration::Scope|X::Declaration::Scope::Multi|X::Does::TypeObject|X::Eval::NoSuchLang|"+
		"X::Export::NameClash|X::IO|X::IO::Chdir|X::IO::Chmod|X::IO::Copy|X::IO::Cwd|X::IO::Dir|"+
		"X::IO::DoesNotExist|X::IO::Link|X::IO::Mkdir|X::IO::Move|X::IO::Rename|X::IO::Rmdir|X::IO::Symlink|"+
		"X::IO::Unlink|X::Inheritance::NotComposed|X::Inheritance::Unsupported|X::Method::InvalidQualifier|"+
		"X::Method::NotFound|X::Method::Private::Permission|X::Method::Private::Unqualified|"+
		"X::Mixin::NotComposable|X::NYI|X::NoDispatcher|X::Numeric::Real|X::OS|X::Obsolete|X::OutOfRange|"+
		"X::Package::Stubbed|X::Parameter::Default|X::Parameter::MultipleTypeConstraints|"+
		"X::Parameter::Placeholder|X::Parameter::Twigil|X::Parameter::WrongOrder|X::Phaser::Multiple|"+
		"X::Phaser::PrePost|X::Placeholder::Block|X::Placeholder::Mainline|X::Pod|X::Proc::Async|"+
		"X::Proc::Async::AlreadyStarted|X::Proc::Async::CharsOrBytes|X::Proc::Async::MustBeStarted|"+
		"X::Proc::Async::OpenForWriting|X::Proc::Async::TapBeforeSpawn|X::Proc::Unsuccessful|"+
		"X::Promise::CauseOnlyValidOnBroken|X::Promise::Vowed|X::Redeclaration|X::Role::Initialization|"+
		"X::Seq::Consumed|X::Sequence::Deduction|X::Signature::NameClash|X::Signature::Placeholder|"+
		"X::Str::Numeric|X::StubCode|X::Syntax|X::Syntax::Augment::WithoutMonkeyTyping|"+
		"X::Syntax::Comment::Embedded|X::Syntax::Confused|X::Syntax::InfixInTermPosition|"+
		"X::Syntax::Malformed|X::Syntax::Missing|X::Syntax::NegatedPair|X::Syntax::NoSelf|"+
		"X::Syntax::Number::RadixOutOfRange|X::Syntax::P5|X::Syntax::Regex::Adverb|"+
		"X::Syntax::Regex::SolitaryQuantifier|X::Syntax::Reserved|X::Syntax::Self::WithoutObject|"+
		"X::Syntax::Signature::InvocantMarker|X::Syntax::Term::MissingInitializer|X::Syntax::UnlessElse|"+
		"X::Syntax::Variable::Match|X::Syntax::Variable::Numeric|X::Syntax::Variable::Twigil|X::Temporal|"+
		"X::Temporal::InvalidFormat|X::TypeCheck|X::TypeCheck::Assignment|X::TypeCheck::Binding|"+
		"X::TypeCheck::Return|X::TypeCheck::Splice|X::Undeclared"
		);

    var builtinFunctions = (
        "abs|abs2rel|absolute|accept|ACCEPTS|accessed|acos|acosec|acosech|acosh|"+
        "acotan|acotanh|acquire|act|action|actions|add|add_attribute|add_enum_value|"+
        "add_fallback|add_method|add_parent|add_private_method|add_role|add_trustee|"+
        "adverb|after|all|allocate|allof|allowed|alternative-names|annotations|antipair|"+
        "antipairs|any|anyof|app_lifetime|append|arch|archname|args|arity|asec|asech|"+
        "asin|asinh|ASSIGN-KEY|ASSIGN-POS|assuming|ast|at|atan|atan2|atanh|AT-KEY|"+
        "atomic-assign|atomic-dec-fetch|atomic-fetch|atomic-fetch-add|atomic-fetch-dec|"+
        "atomic-fetch-inc|atomic-fetch-sub|atomic-inc-fetch|AT-POS|attributes|auth|await|"+
        "backtrace|Bag|BagHash|base|basename|base-repeating|batch|BIND-KEY|BIND-POS|"+
        "bind-stderr|bind-stdin|bind-stdout|bind-udp|bits|bless|block|bool-only|"+
        "bounds|break|Bridge|broken|BUILD|build-date|bytes|cache|callframe|calling-package|"+
        "CALL-ME|callsame|callwith|can|cancel|candidates|cando|canonpath|caps|caption|"+
        "Capture|cas|catdir|categorize|categorize-list|catfile|catpath|cause|ceiling|"+
        "cglobal|changed|Channel|chars|chdir|child|child-name|child-typename|chmod|chomp|"+
        "chop|chr|chrs|chunks|cis|classify|classify-list|cleanup|clone|close|closed|"+
        "close-stdin|code|codes|collate|column|comb|combinations|command|comment|"+
        "compiler|Complex|compose|compose_type|composer|condition|config|configure_destroy|"+
        "configure_type_checking|conj|connect|constraints|construct|contains|contents|copy|"+
        "cos|cosec|cosech|cosh|cotan|cotanh|count|count-only|cpu-cores|cpu-usage|CREATE|"+
        "create_type|cross|cue|curdir|curupdir|d|Date|DateTime|day|daycount|day-of-month|"+
        "day-of-week|day-of-year|days-in-month|declaration|decode|decoder|deepmap|"+
        "defined|DEFINITE|delayed|DELETE-KEY|DELETE-POS|denominator|desc|DESTROY|destroyers|"+
        "devnull|did-you-mean|die|dir|dirname|dir-sep|DISTROnames|do|done|duckmap|dynamic|"+
        "e|eager|earlier|elems|emit|enclosing|encode|encoder|encoding|end|ends-with|enum_from_value|"+
        "enum_value_list|enum_values|enums|eof|EVAL|EVALFILE|exception|excludes-max|excludes-min|"+
        "EXISTS-KEY|EXISTS-POS|exit|exitcode|exp|expected|explicitly-manage|expmod|extension|f|"+
        "fail|fc|feature|file|filename|find_method|find_method_qualified|finish|first|flat|flatmap|"+
        "flip|floor|flush|fmt|format|formatter|freeze|from|from-list|from-loop|from-posix|full|"+
        "full-barrier|get|get_value|getc|gist|got|grab|grabpairs|grep|handle|handled|handles|"+
        "hardware|has_accessor|head|headers|hh-mm-ss|hidden|hides|hour|how|hyper|id|illegal|"+
        "im|in|indent|index|indices|indir|infinite|infix|install_method_cache|"+
        "Instant|instead|int-bounds|interval|in-timezone|invalid-str|invert|invocant|IO|"+
        "IO::Notification.watch-path|is_trusted|is_type|isa|is-absolute|is-hidden|is-initial-thread|"+
        "is-int|is-lazy|is-leap-year|isNaN|is-prime|is-relative|is-routine|is-setting|is-win|item|"+
        "iterator|join|keep|kept|KERNELnames|key|keyof|keys|kill|kv|kxxv|l|lang|last|lastcall|later|"+
        "lazy|lc|leading|level|line|lines|link|listen|live|local|lock|log|log10|lookup|lsb|"+
        "MAIN|match|max|maxpairs|merge|message|method_table|methods|migrate|min|minmax|"+
        "minpairs|minute|misplaced|Mix|MixHash|mkdir|mode|modified|month|move|mro|msb|multiness|"+
        "name|named|named_names|narrow|nativecast|native-descriptor|nativesizeof|new|new_type|"+
        "new-from-daycount|new-from-pairs|next|nextcallee|next-handle|nextsame|nextwith|NFC|NFD|"+
        "NFKC|NFKD|nl-in|nl-out|nodemap|none|norm|not|note|now|nude|numerator|Numeric|of|"+
        "offset|offset-in-hours|offset-in-minutes|old|on-close|one|on-switch|open|opened|"+
        "operation|optional|ord|ords|orig|os-error|osname|out-buffer|pack|package|package-kind|"+
        "package-name|packages|pair|pairs|pairup|parameter|params|parent|parent-name|parents|parse|"+
        "parse-base|parsefile|parse-names|parts|path|path-sep|payload|peer-host|peer-port|periods|"+
        "perl|permutations|phaser|pick|pickpairs|pid|placeholder|plus|polar|poll|polymod|pop|pos|"+
        "positional|posix|postfix|postmatch|precomp-ext|precomp-target|pred|prefix|prematch|prepend|"+
        "print|printf|print-nl|print-to|private|private_method_table|proc|produce|Promise|prompt|"+
        "protect|pull-one|push|push-all|push-at-least|push-exactly|push-until-lazy|put|"+
        "qualifier-type|quit|r|race|radix|rand|range|raw|re|read|readchars|readonly|"+
        "ready|Real|reallocate|reals|reason|rebless|receive|recv|redispatcher|redo|reduce|"+
        "rel2abs|relative|release|rename|repeated|replacement|report|reserved|resolve|"+
        "restore|result|resume|rethrow|reverse|right|rindex|rmdir|roles_to_compose|"+
        "rolish|roll|rootdir|roots|rotate|rotor|round|roundrobin|routine-type|run|rwx|s|"+
        "samecase|samemark|samewith|say|schedule-on|scheduler|scope|sec|sech|second|seek|"+
        "self|send|Set|set_hidden|set_name|set_package|set_rw|set_value|SetHash|"+
        "set-instruments|setup_finalization|shape|share|shell|shift|sibling|sigil|"+
        "sign|signal|signals|signature|sin|sinh|sink|sink-all|skip|skip-at-least|"+
        "skip-at-least-pull-one|skip-one|sleep|sleep-timer|sleep-until|Slip|slurp|"+
        "slurp-rest|slurpy|snap|snapper|so|socket-host|socket-port|sort|source|"+
        "source-package|spawn|SPEC|splice|split|splitdir|splitpath|sprintf|spurt|"+
        "sqrt|squish|srand|stable|start|started|starts-with|status|stderr|stdout|"+
        "sub_signature|subbuf|subbuf-rw|subname|subparse|subst|subst-mutate|"+
        "substr|substr-eq|substr-rw|succ|sum|Supply|symlink|t|tail|take|take-rw|"+
        "tan|tanh|tap|target|target-name|tc|tclc|tell|then|throttle|throw|timezone|"+
        "tmpdir|to|today|toggle|to-posix|total|trailing|trans|tree|trim|trim-leading|"+
        "trim-trailing|truncate|truncated-to|trusts|try_acquire|trying|twigil|type|"+
        "type_captures|typename|uc|udp|uncaught_handler|unimatch|uniname|uninames|"+
        "uniparse|uniprop|uniprops|unique|unival|univals|unlink|unlock|unpack|unpolar|"+
        "unshift|unwrap|updir|USAGE|utc|val|value|values|VAR|variable|verbose-config|"+
        "version|VMnames|volume|vow|w|wait|warn|watch|watch-path|week|weekday-of-month|"+
        "week-number|week-year|WHAT|WHERE|WHEREFORE|WHICH|WHO|whole-second|WHY|"+
        "wordcase|words|workaround|wrap|write|write-to|yada|year|yield|yyyy-mm-dd|"+
        "z|zip|zip-latest|"+
        "plan|done-testing|bail-out|todo|skip|skip-rest|diag|subtest|pass|flunk|ok|"+
        "nok|cmp-ok|is-deeply|isnt|is-approx|like|unlike|use-ok|isa-ok|does-ok|"+
        "can-ok|dies-ok|lives-ok|eval-dies-ok|eval-lives-ok|throws-like|fails-like|"+
		"rw|required|native|repr|export|symbol"
	);
	var constants_ascii = ("pi|Inf|tau|time");
	
	var ops_txt = ("eq|ne|gt|lt|le|ge|div|gcd|lcm|leg|cmp|ff|fff|"+
		"x|before|after|Z|X|and|or|andthen|notandthen|orelse|xor"
	);

	var keywordMapper = this.createKeywordMapper({
		"keyword": keywords,
		"storage.type" : types,
		"constant.language": constants_ascii,
		"support.function": builtinFunctions,
		"keyword.operator": ops_txt
	}, "identifier");
	
	var moduleName = "[a-zA-Z_][a-zA-Z_0-9:-]*\\b";
	var hex = {	token : "constant.numeric", regex : "0x[0-9a-fA-F]+\\b" };
	var num_rat = { token : "constant.numeric", regex : "[+-.]?\\d+(?:(?:\\.\\d*)?(?:[eE][+-]?\\d+)?)?\\b" };
	var num_with_ = { token : "constant.numeric", regex : "(?:\\d+_?\\d+)+\\b" };
	var complex_numbers = { token : "constant.numeric", regex : "\\+?\\d+i\\b" };
	var booleans = { token : "constant.language.boolean", regex : "(?:True|False)\\b" };
	var versions = { token : "constant.other", regex : "v[0-9](?:\\.[a-zA-Z0-9*])*\\b" };
	var lang_keywords = { token : keywordMapper, regex : "[a-zA-Z][\\:a-zA-Z0-9_-]*\\b" };
	var variables = { token : "variable.language", regex : "[$@%&][?*!.]?[a-zA-Z0-9_-]+\\b" };
	var vars_special = { token: "variable.language", regex : "\\$[/|!]?|@\\$/" };
	var ops_char = { token : "keyword.operator", regex : "=|<|>|\\+|\\*|-|/|~|%|\\?|!|\\^|\\.|\\:|\\,|"+
	"»|«|\\||\\&|⚛|∘" };
	var constants_unicode = { token : "constant.language", regex : "𝑒|π|τ|∞" };
	var qstrings = { token : "string.quoted.single", regex : "['](?:(?:\\\\.)|(?:[^'\\\\]))*?[']" };
	var word_quoting = { token : "string.quoted.single", regex : "[<](?:[a-zA-Z0-9 ])*[>]"};
	var regexp = {
				token : "string.regexp",
				regex : "[m|rx]?[/](?:(?:\\[(?:\\\\]|[^\\]])+\\])|(?:\\\\/|[^\\]/]))*[/]\\w*\\s*(?=[).,;]|$)" };
	
	
	this.$rules = {
		"start" : [
			{
				token : "comment.block", // Embedded Comments - Parentheses
				regex : "#[`|=]\\(.*\\)"
			}, {
				token : "comment.block", // Embedded Comments - Brackets
				regex : "#[`|=]\\[.*\\]"
			}, {
				token : "comment.doc", // Multiline Comments
				regex : "^=(?:begin)\\b",
				next : "block_comment"
			}, {
				token : "string.unquoted", // q Heredocs
				regex : "q[x|w]?\\:to/END/;",
				next : "qheredoc"
			}, {
				token : "string.unquoted", // qq Heredocs
				regex : "qq[x|w]?\\:to/END/;",
				next : "qqheredoc"
			},
			regexp,
			qstrings
			, {
				token : "string.quoted.double", // Double Quoted String
				regex : '"',
				next : "qqstring"
			},
			word_quoting
			, {
				token: ["keyword", "text", "variable.module"], // use - Module Names, Pragmas, etc.
				regex: "(use)(\\s+)((?:"+moduleName+"\\.?)*)"
			},
			hex,
			num_rat,
			num_with_,
			complex_numbers,
			booleans,
			versions,
			lang_keywords,
			variables,
			vars_special,
			ops_char,
			constants_unicode
			, {
				token : "comment", // Sigle Line Comments
				regex : "#.*$"
			}, {
				token : "lparen",
				regex : "[[({]"
			}, {
				token : "rparen",
				regex : "[\\])}]"
			}, {
				token : "text",
				regex : "\\s+"
			}
		],
		"qqstring" : [
			{
				token : "constant.language.escape",
				regex : '\\\\(?:[nrtef\\\\"$]|[0-7]{1,3}|x[0-9A-Fa-f]{1,2})'
			}, 
			variables,
			vars_special
			, {
				token : "lparen",
				regex : "{",
				next : "qqinterpolation"
			}, {
				token : "string.quoted.double", 
				regex : '"', 
				next : "start"
			}, {
				defaultToken : "string.quoted.double"
			}
		],
		"qqinterpolation" : [
			hex,
			num_rat,
			num_with_,
			complex_numbers,
			booleans,
			versions,
			lang_keywords,
			variables,
			vars_special,
			ops_char,
			constants_unicode,
			qstrings,
			regexp,
			
			{
				token: "rparen",
				regex: "}",
				next : "qqstring"
			}
		],
		"block_comment": [
			{
				token: "comment.doc",
				regex: "^=end +[a-zA-Z_0-9]*",
				next: "start"
			},
			{
				defaultToken: "comment.doc"
			}
		],
		"qheredoc": [
			{
				token: "string.unquoted",
				regex: "END$",
				next: "start"
			}, {
				defaultToken: "string.unquoted"
			}
		],
		"qqheredoc": [
			variables,
			vars_special,
			{
				token : "lparen",
				regex : "{",
				next : "qqheredocinterpolation"
			}, {
				token: "string.unquoted",
				regex: "END$",
				next: "start"
			}, {
				defaultToken: "string.unquoted"
			}
		],
		"qqheredocinterpolation" : [
			hex,
			num_rat,
			num_with_,
			complex_numbers,
			booleans,
			versions,
			lang_keywords,
			variables,
			vars_special,
			ops_char,
			constants_unicode,
			qstrings,
			regexp,
			{
				token: "rparen",
				regex: "}",
				next : "qqheredoc"
			}
		]
	};
};

oop.inherits(Perl6HighlightRules, TextHighlightRules);

exports.Perl6HighlightRules = Perl6HighlightRules;
});

define("ace/mode/matching_brace_outdent",["require","exports","module","ace/range"], function(require, exports, module) {
"use strict";

var Range = require("../range").Range;

var MatchingBraceOutdent = function() {};

(function() {

    this.checkOutdent = function(line, input) {
        if (! /^\s+$/.test(line))
            return false;

        return /^\s*\}/.test(input);
    };

    this.autoOutdent = function(doc, row) {
        var line = doc.getLine(row);
        var match = line.match(/^(\s*\})/);

        if (!match) return 0;

        var column = match[1].length;
        var openBracePos = doc.findMatchingBracket({row: row, column: column});

        if (!openBracePos || openBracePos.row == row) return 0;

        var indent = this.$getIndent(doc.getLine(openBracePos.row));
        doc.replace(new Range(row, 0, row, column-1), indent);
    };

    this.$getIndent = function(line) {
        return line.match(/^\s*/)[0];
    };

}).call(MatchingBraceOutdent.prototype);

exports.MatchingBraceOutdent = MatchingBraceOutdent;
});

define("ace/mode/folding/cstyle",["require","exports","module","ace/lib/oop","ace/range","ace/mode/folding/fold_mode"], function(require, exports, module) {
"use strict";

var oop = require("../../lib/oop");
var Range = require("../../range").Range;
var BaseFoldMode = require("./fold_mode").FoldMode;

var FoldMode = exports.FoldMode = function(commentRegex) {
    if (commentRegex) {
        this.foldingStartMarker = new RegExp(
            this.foldingStartMarker.source.replace(/\|[^|]*?$/, "|" + commentRegex.start)
        );
        this.foldingStopMarker = new RegExp(
            this.foldingStopMarker.source.replace(/\|[^|]*?$/, "|" + commentRegex.end)
        );
    }
};
oop.inherits(FoldMode, BaseFoldMode);

(function() {
    
    this.foldingStartMarker = /([\{\[\(])[^\}\]\)]*$|^\s*(\/\*)/;
    this.foldingStopMarker = /^[^\[\{\(]*([\}\]\)])|^[\s\*]*(\*\/)/;
    this.singleLineBlockCommentRe= /^\s*(\/\*).*\*\/\s*$/;
    this.tripleStarBlockCommentRe = /^\s*(\/\*\*\*).*\*\/\s*$/;
    this.startRegionRe = /^\s*(\/\*|\/\/)#?region\b/;
    this._getFoldWidgetBase = this.getFoldWidget;
    this.getFoldWidget = function(session, foldStyle, row) {
        var line = session.getLine(row);
    
        if (this.singleLineBlockCommentRe.test(line)) {
            if (!this.startRegionRe.test(line) && !this.tripleStarBlockCommentRe.test(line))
                return "";
        }
    
        var fw = this._getFoldWidgetBase(session, foldStyle, row);
    
        if (!fw && this.startRegionRe.test(line))
            return "start"; // lineCommentRegionStart
    
        return fw;
    };

    this.getFoldWidgetRange = function(session, foldStyle, row, forceMultiline) {
        var line = session.getLine(row);
        
        if (this.startRegionRe.test(line))
            return this.getCommentRegionBlock(session, line, row);
        
        var match = line.match(this.foldingStartMarker);
        if (match) {
            var i = match.index;

            if (match[1])
                return this.openingBracketBlock(session, match[1], row, i);
                
            var range = session.getCommentFoldRange(row, i + match[0].length, 1);
            
            if (range && !range.isMultiLine()) {
                if (forceMultiline) {
                    range = this.getSectionRange(session, row);
                } else if (foldStyle != "all")
                    range = null;
            }
            
            return range;
        }

        if (foldStyle === "markbegin")
            return;

        var match = line.match(this.foldingStopMarker);
        if (match) {
            var i = match.index + match[0].length;

            if (match[1])
                return this.closingBracketBlock(session, match[1], row, i);

            return session.getCommentFoldRange(row, i, -1);
        }
    };
    
    this.getSectionRange = function(session, row) {
        var line = session.getLine(row);
        var startIndent = line.search(/\S/);
        var startRow = row;
        var startColumn = line.length;
        row = row + 1;
        var endRow = row;
        var maxRow = session.getLength();
        while (++row < maxRow) {
            line = session.getLine(row);
            var indent = line.search(/\S/);
            if (indent === -1)
                continue;
            if  (startIndent > indent)
                break;
            var subRange = this.getFoldWidgetRange(session, "all", row);
            
            if (subRange) {
                if (subRange.start.row <= startRow) {
                    break;
                } else if (subRange.isMultiLine()) {
                    row = subRange.end.row;
                } else if (startIndent == indent) {
                    break;
                }
            }
            endRow = row;
        }
        
        return new Range(startRow, startColumn, endRow, session.getLine(endRow).length);
    };
    this.getCommentRegionBlock = function(session, line, row) {
        var startColumn = line.search(/\s*$/);
        var maxRow = session.getLength();
        var startRow = row;
        
        var re = /^\s*(?:\/\*|\/\/|--)#?(end)?region\b/;
        var depth = 1;
        while (++row < maxRow) {
            line = session.getLine(row);
            var m = re.exec(line);
            if (!m) continue;
            if (m[1]) depth--;
            else depth++;

            if (!depth) break;
        }

        var endRow = row;
        if (endRow > startRow) {
            return new Range(startRow, startColumn, endRow, line.length);
        }
    };

}).call(FoldMode.prototype);

});

define("ace/mode/perl6",["require","exports","module","ace/lib/oop","ace/mode/text","ace/mode/perl6_highlight_rules","ace/mode/matching_brace_outdent","ace/mode/folding/cstyle"], function(require, exports, module) {
"use strict";

var oop = require("../lib/oop");
var TextMode = require("./text").Mode;
var Perl6HighlightRules = require("./perl6_highlight_rules").Perl6HighlightRules;
var MatchingBraceOutdent = require("./matching_brace_outdent").MatchingBraceOutdent;
var CStyleFoldMode = require("./folding/cstyle").FoldMode;

var Mode = function() {
    this.HighlightRules = Perl6HighlightRules;

    this.$outdent = new MatchingBraceOutdent();
    this.foldingRules = new CStyleFoldMode({start: "^=(begin)\\b", end: "^=(end)\\b"});
    this.$behaviour = this.$defaultBehaviour;
};
oop.inherits(Mode, TextMode);

(function() {

    this.lineCommentStart = "#";
    this.blockComment = [
        {start: "=begin", end: "=end", lineStartOnly: true},
        {start: "=item", end: "=end", lineStartOnly: true}
    ];


    this.getNextLineIndent = function(state, line, tab) {
        var indent = this.$getIndent(line);

        var tokenizedLine = this.getTokenizer().getLineTokens(line, state);
        var tokens = tokenizedLine.tokens;

        if (tokens.length && tokens[tokens.length-1].type == "comment") {
            return indent;
        }

        if (state == "start") {
            var match = line.match(/^.*[\{\(\[:]\s*$/);
            if (match) {
                indent += tab;
            }
        }

        return indent;
    };

    this.checkOutdent = function(state, line, input) {
        return this.$outdent.checkOutdent(line, input);
    };

    this.autoOutdent = function(state, doc, row) {
        this.$outdent.autoOutdent(doc, row);
    };

    this.$id = "ace/mode/perl6";
}).call(Mode.prototype);

exports.Mode = Mode;
});                (function() {
                    window.require(["ace/mode/perl6"], function(m) {
                        if (typeof module == "object" && typeof exports == "object" && module) {
                            module.exports = m;
                        }
                    });
                })();
            