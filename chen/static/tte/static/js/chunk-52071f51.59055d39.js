(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-52071f51"], {
        "0dd0": function(e, t, n) {},
        "3f23": function(e, t) {
            e.exports = '/* Jison generated parser */\nvar jsonlint = (function(){\nvar parser = {trace: function trace() { },\nyy: {},\nsymbols_: {"error":2,"JSONString":3,"STRING":4,"JSONNumber":5,"NUMBER":6,"JSONNullLiteral":7,"NULL":8,"JSONBooleanLiteral":9,"TRUE":10,"FALSE":11,"JSONText":12,"JSONValue":13,"EOF":14,"JSONObject":15,"JSONArray":16,"{":17,"}":18,"JSONMemberList":19,"JSONMember":20,":":21,",":22,"[":23,"]":24,"JSONElementList":25,"$accept":0,"$end":1},\nterminals_: {2:"error",4:"STRING",6:"NUMBER",8:"NULL",10:"TRUE",11:"FALSE",14:"EOF",17:"{",18:"}",21:":",22:",",23:"[",24:"]"},\nproductions_: [0,[3,1],[5,1],[7,1],[9,1],[9,1],[12,2],[13,1],[13,1],[13,1],[13,1],[13,1],[13,1],[15,2],[15,3],[20,3],[19,1],[19,3],[16,2],[16,3],[25,1],[25,3]],\nperformAction: function anonymous(yytext,yyleng,yylineno,yy,yystate,$$,_$) {\n\nvar $0 = $$.length - 1;\nswitch (yystate) {\ncase 1: // replace escaped characters with actual character\n          this.$ = yytext.replace(/\\\\(\\\\|")/g, "$"+"1")\n                     .replace(/\\\\n/g,\'\\n\')\n                     .replace(/\\\\r/g,\'\\r\')\n                     .replace(/\\\\t/g,\'\\t\')\n                     .replace(/\\\\v/g,\'\\v\')\n                     .replace(/\\\\f/g,\'\\f\')\n                     .replace(/\\\\b/g,\'\\b\');\n        \nbreak;\ncase 2:this.$ = Number(yytext);\nbreak;\ncase 3:this.$ = null;\nbreak;\ncase 4:this.$ = true;\nbreak;\ncase 5:this.$ = false;\nbreak;\ncase 6:return this.$ = $$[$0-1];\nbreak;\ncase 13:this.$ = {};\nbreak;\ncase 14:this.$ = $$[$0-1];\nbreak;\ncase 15:this.$ = [$$[$0-2], $$[$0]];\nbreak;\ncase 16:this.$ = {}; this.$[$$[$0][0]] = $$[$0][1];\nbreak;\ncase 17:this.$ = $$[$0-2]; $$[$0-2][$$[$0][0]] = $$[$0][1];\nbreak;\ncase 18:this.$ = [];\nbreak;\ncase 19:this.$ = $$[$0-1];\nbreak;\ncase 20:this.$ = [$$[$0]];\nbreak;\ncase 21:this.$ = $$[$0-2]; $$[$0-2].push($$[$0]);\nbreak;\n}\n},\ntable: [{3:5,4:[1,12],5:6,6:[1,13],7:3,8:[1,9],9:4,10:[1,10],11:[1,11],12:1,13:2,15:7,16:8,17:[1,14],23:[1,15]},{1:[3]},{14:[1,16]},{14:[2,7],18:[2,7],22:[2,7],24:[2,7]},{14:[2,8],18:[2,8],22:[2,8],24:[2,8]},{14:[2,9],18:[2,9],22:[2,9],24:[2,9]},{14:[2,10],18:[2,10],22:[2,10],24:[2,10]},{14:[2,11],18:[2,11],22:[2,11],24:[2,11]},{14:[2,12],18:[2,12],22:[2,12],24:[2,12]},{14:[2,3],18:[2,3],22:[2,3],24:[2,3]},{14:[2,4],18:[2,4],22:[2,4],24:[2,4]},{14:[2,5],18:[2,5],22:[2,5],24:[2,5]},{14:[2,1],18:[2,1],21:[2,1],22:[2,1],24:[2,1]},{14:[2,2],18:[2,2],22:[2,2],24:[2,2]},{3:20,4:[1,12],18:[1,17],19:18,20:19},{3:5,4:[1,12],5:6,6:[1,13],7:3,8:[1,9],9:4,10:[1,10],11:[1,11],13:23,15:7,16:8,17:[1,14],23:[1,15],24:[1,21],25:22},{1:[2,6]},{14:[2,13],18:[2,13],22:[2,13],24:[2,13]},{18:[1,24],22:[1,25]},{18:[2,16],22:[2,16]},{21:[1,26]},{14:[2,18],18:[2,18],22:[2,18],24:[2,18]},{22:[1,28],24:[1,27]},{22:[2,20],24:[2,20]},{14:[2,14],18:[2,14],22:[2,14],24:[2,14]},{3:20,4:[1,12],20:29},{3:5,4:[1,12],5:6,6:[1,13],7:3,8:[1,9],9:4,10:[1,10],11:[1,11],13:30,15:7,16:8,17:[1,14],23:[1,15]},{14:[2,19],18:[2,19],22:[2,19],24:[2,19]},{3:5,4:[1,12],5:6,6:[1,13],7:3,8:[1,9],9:4,10:[1,10],11:[1,11],13:31,15:7,16:8,17:[1,14],23:[1,15]},{18:[2,17],22:[2,17]},{18:[2,15],22:[2,15]},{22:[2,21],24:[2,21]}],\ndefaultActions: {16:[2,6]},\nparseError: function parseError(str, hash) {\n    throw new Error(str);\n},\nparse: function parse(input) {\n    var self = this,\n        stack = [0],\n        vstack = [null], // semantic value stack\n        lstack = [], // location stack\n        table = this.table,\n        yytext = \'\',\n        yylineno = 0,\n        yyleng = 0,\n        recovering = 0,\n        TERROR = 2,\n        EOF = 1;\n\n    //this.reductionCount = this.shiftCount = 0;\n\n    this.lexer.setInput(input);\n    this.lexer.yy = this.yy;\n    this.yy.lexer = this.lexer;\n    if (typeof this.lexer.yylloc == \'undefined\')\n        this.lexer.yylloc = {};\n    var yyloc = this.lexer.yylloc;\n    lstack.push(yyloc);\n\n    if (typeof this.yy.parseError === \'function\')\n        this.parseError = this.yy.parseError;\n\n    function popStack (n) {\n        stack.length = stack.length - 2*n;\n        vstack.length = vstack.length - n;\n        lstack.length = lstack.length - n;\n    }\n\n    function lex() {\n        var token;\n        token = self.lexer.lex() || 1; // $end = 1\n        // if token isn\'t its numeric value, convert\n        if (typeof token !== \'number\') {\n            token = self.symbols_[token] || token;\n        }\n        return token;\n    }\n\n    var symbol, preErrorSymbol, state, action, a, r, yyval={},p,len,newState, expected;\n    while (true) {\n        // retreive state number from top of stack\n        state = stack[stack.length-1];\n\n        // use default actions if available\n        if (this.defaultActions[state]) {\n            action = this.defaultActions[state];\n        } else {\n            if (symbol == null)\n                symbol = lex();\n            // read action for current state and first input\n            action = table[state] && table[state][symbol];\n        }\n\n        // handle parse error\n        _handle_error:\n        if (typeof action === \'undefined\' || !action.length || !action[0]) {\n\n            if (!recovering) {\n                // Report error\n                expected = [];\n                for (p in table[state]) if (this.terminals_[p] && p > 2) {\n                    expected.push("\'"+this.terminals_[p]+"\'");\n                }\n                var errStr = \'\';\n                if (this.lexer.showPosition) {\n                    errStr = \'Parse error on line \'+(yylineno+1)+":\\n"+this.lexer.showPosition()+"\\nExpecting "+expected.join(\', \') + ", got \'" + this.terminals_[symbol]+ "\'";\n                } else {\n                    errStr = \'Parse error on line \'+(yylineno+1)+": Unexpected " +\n                                  (symbol == 1 /*EOF*/ ? "end of input" :\n                                              ("\'"+(this.terminals_[symbol] || symbol)+"\'"));\n                }\n                this.parseError(errStr,\n                    {text: this.lexer.match, token: this.terminals_[symbol] || symbol, line: this.lexer.yylineno, loc: yyloc, expected: expected});\n            }\n\n            // just recovered from another error\n            if (recovering == 3) {\n                if (symbol == EOF) {\n                    throw new Error(errStr || \'Parsing halted.\');\n                }\n\n                // discard current lookahead and grab another\n                yyleng = this.lexer.yyleng;\n                yytext = this.lexer.yytext;\n                yylineno = this.lexer.yylineno;\n                yyloc = this.lexer.yylloc;\n                symbol = lex();\n            }\n\n            // try to recover from error\n            while (1) {\n                // check for error recovery rule in this state\n                if ((TERROR.toString()) in table[state]) {\n                    break;\n                }\n                if (state == 0) {\n                    throw new Error(errStr || \'Parsing halted.\');\n                }\n                popStack(1);\n                state = stack[stack.length-1];\n            }\n\n            preErrorSymbol = symbol; // save the lookahead token\n            symbol = TERROR;         // insert generic error symbol as new lookahead\n            state = stack[stack.length-1];\n            action = table[state] && table[state][TERROR];\n            recovering = 3; // allow 3 real symbols to be shifted before reporting a new error\n        }\n\n        // this shouldn\'t happen, unless resolve defaults are off\n        if (action[0] instanceof Array && action.length > 1) {\n            throw new Error(\'Parse Error: multiple actions possible at state: \'+state+\', token: \'+symbol);\n        }\n\n        switch (action[0]) {\n\n            case 1: // shift\n                //this.shiftCount++;\n\n                stack.push(symbol);\n                vstack.push(this.lexer.yytext);\n                lstack.push(this.lexer.yylloc);\n                stack.push(action[1]); // push state\n                symbol = null;\n                if (!preErrorSymbol) { // normal execution/no error\n                    yyleng = this.lexer.yyleng;\n                    yytext = this.lexer.yytext;\n                    yylineno = this.lexer.yylineno;\n                    yyloc = this.lexer.yylloc;\n                    if (recovering > 0)\n                        recovering--;\n                } else { // error just occurred, resume old lookahead f/ before error\n                    symbol = preErrorSymbol;\n                    preErrorSymbol = null;\n                }\n                break;\n\n            case 2: // reduce\n                //this.reductionCount++;\n\n                len = this.productions_[action[1]][1];\n\n                // perform semantic action\n                yyval.$ = vstack[vstack.length-len]; // default to $$ = $1\n                // default location, uses first token for firsts, last for lasts\n                yyval._$ = {\n                    first_line: lstack[lstack.length-(len||1)].first_line,\n                    last_line: lstack[lstack.length-1].last_line,\n                    first_column: lstack[lstack.length-(len||1)].first_column,\n                    last_column: lstack[lstack.length-1].last_column\n                };\n                r = this.performAction.call(yyval, yytext, yyleng, yylineno, this.yy, action[1], vstack, lstack);\n\n                if (typeof r !== \'undefined\') {\n                    return r;\n                }\n\n                // pop off stack\n                if (len) {\n                    stack = stack.slice(0,-1*len*2);\n                    vstack = vstack.slice(0, -1*len);\n                    lstack = lstack.slice(0, -1*len);\n                }\n\n                stack.push(this.productions_[action[1]][0]);    // push nonterminal (reduce)\n                vstack.push(yyval.$);\n                lstack.push(yyval._$);\n                // goto new state = table[STATE][NONTERMINAL]\n                newState = table[stack[stack.length-2]][stack[stack.length-1]];\n                stack.push(newState);\n                break;\n\n            case 3: // accept\n                return true;\n        }\n\n    }\n\n    return true;\n}};\n/* Jison generated lexer */\nvar lexer = (function(){\nvar lexer = ({EOF:1,\nparseError:function parseError(str, hash) {\n        if (this.yy.parseError) {\n            this.yy.parseError(str, hash);\n        } else {\n            throw new Error(str);\n        }\n    },\nsetInput:function (input) {\n        this._input = input;\n        this._more = this._less = this.done = false;\n        this.yylineno = this.yyleng = 0;\n        this.yytext = this.matched = this.match = \'\';\n        this.conditionStack = [\'INITIAL\'];\n        this.yylloc = {first_line:1,first_column:0,last_line:1,last_column:0};\n        return this;\n    },\ninput:function () {\n        var ch = this._input[0];\n        this.yytext+=ch;\n        this.yyleng++;\n        this.match+=ch;\n        this.matched+=ch;\n        var lines = ch.match(/\\n/);\n        if (lines) this.yylineno++;\n        this._input = this._input.slice(1);\n        return ch;\n    },\nunput:function (ch) {\n        this._input = ch + this._input;\n        return this;\n    },\nmore:function () {\n        this._more = true;\n        return this;\n    },\nless:function (n) {\n        this._input = this.match.slice(n) + this._input;\n    },\npastInput:function () {\n        var past = this.matched.substr(0, this.matched.length - this.match.length);\n        return (past.length > 20 ? \'...\':\'\') + past.substr(-20).replace(/\\n/g, "");\n    },\nupcomingInput:function () {\n        var next = this.match;\n        if (next.length < 20) {\n            next += this._input.substr(0, 20-next.length);\n        }\n        return (next.substr(0,20)+(next.length > 20 ? \'...\':\'\')).replace(/\\n/g, "");\n    },\nshowPosition:function () {\n        var pre = this.pastInput();\n        var c = new Array(pre.length + 1).join("-");\n        return pre + this.upcomingInput() + "\\n" + c+"^";\n    },\nnext:function () {\n        if (this.done) {\n            return this.EOF;\n        }\n        if (!this._input) this.done = true;\n\n        var token,\n            match,\n            tempMatch,\n            index,\n            col,\n            lines;\n        if (!this._more) {\n            this.yytext = \'\';\n            this.match = \'\';\n        }\n        var rules = this._currentRules();\n        for (var i=0;i < rules.length; i++) {\n            tempMatch = this._input.match(this.rules[rules[i]]);\n            if (tempMatch && (!match || tempMatch[0].length > match[0].length)) {\n                match = tempMatch;\n                index = i;\n                if (!this.options.flex) break;\n            }\n        }\n        if (match) {\n            lines = match[0].match(/\\n.*/g);\n            if (lines) this.yylineno += lines.length;\n            this.yylloc = {first_line: this.yylloc.last_line,\n                           last_line: this.yylineno+1,\n                           first_column: this.yylloc.last_column,\n                           last_column: lines ? lines[lines.length-1].length-1 : this.yylloc.last_column + match[0].length}\n            this.yytext += match[0];\n            this.match += match[0];\n            this.yyleng = this.yytext.length;\n            this._more = false;\n            this._input = this._input.slice(match[0].length);\n            this.matched += match[0];\n            token = this.performAction.call(this, this.yy, this, rules[index],this.conditionStack[this.conditionStack.length-1]);\n            if (this.done && this._input) this.done = false;\n            if (token) return token;\n            else return;\n        }\n        if (this._input === "") {\n            return this.EOF;\n        } else {\n            this.parseError(\'Lexical error on line \'+(this.yylineno+1)+\'. Unrecognized text.\\n\'+this.showPosition(), \n                    {text: "", token: null, line: this.yylineno});\n        }\n    },\nlex:function lex() {\n        var r = this.next();\n        if (typeof r !== \'undefined\') {\n            return r;\n        } else {\n            return this.lex();\n        }\n    },\nbegin:function begin(condition) {\n        this.conditionStack.push(condition);\n    },\npopState:function popState() {\n        return this.conditionStack.pop();\n    },\n_currentRules:function _currentRules() {\n        return this.conditions[this.conditionStack[this.conditionStack.length-1]].rules;\n    },\ntopState:function () {\n        return this.conditionStack[this.conditionStack.length-2];\n    },\npushState:function begin(condition) {\n        this.begin(condition);\n    }});\nlexer.options = {};\nlexer.performAction = function anonymous(yy,yy_,$avoiding_name_collisions,YY_START) {\n\nvar YYSTATE=YY_START\nswitch($avoiding_name_collisions) {\ncase 0:/* skip whitespace */\nbreak;\ncase 1:return 6\nbreak;\ncase 2:yy_.yytext = yy_.yytext.substr(1,yy_.yyleng-2); return 4\nbreak;\ncase 3:return 17\nbreak;\ncase 4:return 18\nbreak;\ncase 5:return 23\nbreak;\ncase 6:return 24\nbreak;\ncase 7:return 22\nbreak;\ncase 8:return 21\nbreak;\ncase 9:return 10\nbreak;\ncase 10:return 11\nbreak;\ncase 11:return 8\nbreak;\ncase 12:return 14\nbreak;\ncase 13:return \'INVALID\'\nbreak;\n}\n};\nlexer.rules = [/^(?:\\s+)/,/^(?:(-?([0-9]|[1-9][0-9]+))(\\.[0-9]+)?([eE][-+]?[0-9]+)?\\b)/,/^(?:"(?:\\\\[\\\\"bfnrt/]|\\\\u[a-fA-F0-9]{4}|[^\\\\\\0-\\x09\\x0a-\\x1f"])*")/,/^(?:\\{)/,/^(?:\\})/,/^(?:\\[)/,/^(?:\\])/,/^(?:,)/,/^(?::)/,/^(?:true\\b)/,/^(?:false\\b)/,/^(?:null\\b)/,/^(?:$)/,/^(?:.)/];\nlexer.conditions = {"INITIAL":{"rules":[0,1,2,3,4,5,6,7,8,9,10,11,12,13],"inclusive":true}};\n\n\n;\nreturn lexer;})()\nparser.lexer = lexer;\nreturn parser;\n})();\nif (typeof require !== \'undefined\' && typeof exports !== \'undefined\') {\nexports.parser = jsonlint;\nexports.parse = function () { return jsonlint.parse.apply(jsonlint, arguments); }\nexports.main = function commonjsMain(args) {\n    if (!args[1])\n        throw new Error(\'Usage: \'+args[0]+\' FILE\');\n    if (typeof process !== \'undefined\') {\n        var source = require(\'fs\').readFileSync(require(\'path\').join(process.cwd(), args[1]), "utf8");\n    } else {\n        var cwd = require("file").path(require("file").cwd());\n        var source = cwd.join(args[1]).read({charset: "utf-8"});\n    }\n    return exports.parser.parse(source);\n}\nif (typeof module !== \'undefined\' && require.main === module) {\n  exports.main(typeof process !== \'undefined\' ? process.argv.slice(1) : require("system").args);\n}\n}'
        },
        "56b3": function(e, t, n) {
            (function(t, n) {
                e.exports = n()
            })(0, (function() {
                "use strict";
                var e = navigator.userAgent,
                    t = navigator.platform,
                    n = /gecko\/\d/i.test(e),
                    r = /MSIE \d/.test(e),
                    i = /Trident\/(?:[7-9]|\d{2,})\..*rv:(\d+)/.exec(e),
                    o = /Edge\/(\d+)/.exec(e),
                    l = r || i || o,
                    a = l && (r ? document.documentMode || 6 : +(o || i)[1]),
                    s = !o && /WebKit\//.test(e),
                    u = s && /Qt\/\d+\.\d+/.test(e),
                    c = !o && /Chrome\//.test(e),
                    f = /Opera\//.test(e),
                    h = /Apple Computer/.test(navigator.vendor),
                    d = /Mac OS X 1\d\D([8-9]|\d\d)\D/.test(e),
                    p = /PhantomJS/.test(e),
                    g = !o && /AppleWebKit/.test(e) && /Mobile\/\w+/.test(e),
                    v = /Android/.test(e),
                    m = g || v || /webOS|BlackBerry|Opera Mini|Opera Mobi|IEMobile/i.test(e),
                    y = g || /Mac/.test(t),
                    b = /\bCrOS\b/.test(e),
                    w = /win/i.test(t),
                    x = f && e.match(/Version\/(\d*\.\d*)/);
                x && (x = Number(x[1])), x && x >= 15 && (f = !1, s = !0);
                var k = y && (u || f && (null == x || x < 12.11)),
                    C = n || l && a >= 9;

                function S(e) {
                    return new RegExp("(^|\\s)" + e + "(?:$|\\s)\\s*")
                }
                var L, T = function(e, t) {
                    var n = e.className,
                        r = S(t).exec(n);
                    if (r) {
                        var i = n.slice(r.index + r[0].length);
                        e.className = n.slice(0, r.index) + (i ? r[1] + i : "")
                    }
                };

                function M(e) {
                    for (var t = e.childNodes.length; t > 0; --t) e.removeChild(e.firstChild);
                    return e
                }

                function N(e, t) {
                    return M(e).appendChild(t)
                }

                function O(e, t, n, r) {
                    var i = document.createElement(e);
                    if (n && (i.className = n), r && (i.style.cssText = r), "string" == typeof t) i.appendChild(document.createTextNode(t));
                    else if (t)
                        for (var o = 0; o < t.length; ++o) i.appendChild(t[o]);
                    return i
                }

                function A(e, t, n, r) {
                    var i = O(e, t, n, r);
                    return i.setAttribute("role", "presentation"), i
                }

                function D(e, t) {
                    if (3 == t.nodeType && (t = t.parentNode), e.contains) return e.contains(t);
                    do {
                        if (11 == t.nodeType && (t = t.host), t == e) return !0
                    } while (t = t.parentNode)
                }

                function E() {
                    var e;
                    try {
                        e = document.activeElement
                    } catch (t) {
                        e = document.body || null
                    }
                    while (e && e.shadowRoot && e.shadowRoot.activeElement) e = e.shadowRoot.activeElement;
                    return e
                }

                function W(e, t) {
                    var n = e.className;
                    S(t).test(n) || (e.className += (n ? " " : "") + t)
                }

                function H(e, t) {
                    for (var n = e.split(" "), r = 0; r < n.length; r++) n[r] && !S(n[r]).test(t) && (t += " " + n[r]);
                    return t
                }
                L = document.createRange ? function(e, t, n, r) {
                    var i = document.createRange();
                    return i.setEnd(r || e, n), i.setStart(e, t), i
                } : function(e, t, n) {
                    var r = document.body.createTextRange();
                    try {
                        r.moveToElementText(e.parentNode)
                    } catch (i) {
                        return r
                    }
                    return r.collapse(!0), r.moveEnd("character", n), r.moveStart("character", t), r
                };
                var F = function(e) {
                    e.select()
                };

                function I(e) {
                    var t = Array.prototype.slice.call(arguments, 1);
                    return function() {
                        return e.apply(null, t)
                    }
                }

                function P(e, t, n) {
                    for (var r in t || (t = {}), e) !e.hasOwnProperty(r) || !1 === n && t.hasOwnProperty(r) || (t[r] = e[r]);
                    return t
                }

                function R(e, t, n, r, i) {
                    null == t && (t = e.search(/[^\s\u00a0]/), -1 == t && (t = e.length));
                    for (var o = r || 0, l = i || 0;;) {
                        var a = e.indexOf("\t", o);
                        if (a < 0 || a >= t) return l + (t - o);
                        l += a - o, l += n - l % n, o = a + 1
                    }
                }
                g ? F = function(e) {
                    e.selectionStart = 0, e.selectionEnd = e.value.length
                } : l && (F = function(e) {
                    try {
                        e.select()
                    } catch (t) {}
                });
                var z = function() {
                    this.id = null
                };

                function B(e, t) {
                    for (var n = 0; n < e.length; ++n)
                        if (e[n] == t) return n;
                    return -1
                }
                z.prototype.set = function(e, t) {
                    clearTimeout(this.id), this.id = setTimeout(t, e)
                };
                var $ = 30,
                    _ = {
                        toString: function() {
                            return "CodeMirror.Pass"
                        }
                    },
                    j = {
                        scroll: !1
                    },
                    G = {
                        origin: "*mouse"
                    },
                    V = {
                        origin: "+move"
                    };

                function U(e, t, n) {
                    for (var r = 0, i = 0;;) {
                        var o = e.indexOf("\t", r); - 1 == o && (o = e.length);
                        var l = o - r;
                        if (o == e.length || i + l >= t) return r + Math.min(l, t - i);
                        if (i += o - r, i += n - i % n, r = o + 1, i >= t) return r
                    }
                }
                var K = [""];

                function Y(e) {
                    while (K.length <= e) K.push(X(K) + " ");
                    return K[e]
                }

                function X(e) {
                    return e[e.length - 1]
                }

                function q(e, t) {
                    for (var n = [], r = 0; r < e.length; r++) n[r] = t(e[r], r);
                    return n
                }

                function J(e, t, n) {
                    var r = 0,
                        i = n(t);
                    while (r < e.length && n(e[r]) <= i) r++;
                    e.splice(r, 0, t)
                }

                function Z() {}

                function Q(e, t) {
                    var n;
                    return Object.create ? n = Object.create(e) : (Z.prototype = e, n = new Z), t && P(t, n), n
                }
                var ee = /[\u00df\u0587\u0590-\u05f4\u0600-\u06ff\u3040-\u309f\u30a0-\u30ff\u3400-\u4db5\u4e00-\u9fcc\uac00-\ud7af]/;

                function te(e) {
                    return /\w/.test(e) || e > "" && (e.toUpperCase() != e.toLowerCase() || ee.test(e))
                }

                function ne(e, t) {
                    return t ? !!(t.source.indexOf("\\w") > -1 && te(e)) || t.test(e) : te(e)
                }

                function re(e) {
                    for (var t in e)
                        if (e.hasOwnProperty(t) && e[t]) return !1;
                    return !0
                }
                var ie = /[\u0300-\u036f\u0483-\u0489\u0591-\u05bd\u05bf\u05c1\u05c2\u05c4\u05c5\u05c7\u0610-\u061a\u064b-\u065e\u0670\u06d6-\u06dc\u06de-\u06e4\u06e7\u06e8\u06ea-\u06ed\u0711\u0730-\u074a\u07a6-\u07b0\u07eb-\u07f3\u0816-\u0819\u081b-\u0823\u0825-\u0827\u0829-\u082d\u0900-\u0902\u093c\u0941-\u0948\u094d\u0951-\u0955\u0962\u0963\u0981\u09bc\u09be\u09c1-\u09c4\u09cd\u09d7\u09e2\u09e3\u0a01\u0a02\u0a3c\u0a41\u0a42\u0a47\u0a48\u0a4b-\u0a4d\u0a51\u0a70\u0a71\u0a75\u0a81\u0a82\u0abc\u0ac1-\u0ac5\u0ac7\u0ac8\u0acd\u0ae2\u0ae3\u0b01\u0b3c\u0b3e\u0b3f\u0b41-\u0b44\u0b4d\u0b56\u0b57\u0b62\u0b63\u0b82\u0bbe\u0bc0\u0bcd\u0bd7\u0c3e-\u0c40\u0c46-\u0c48\u0c4a-\u0c4d\u0c55\u0c56\u0c62\u0c63\u0cbc\u0cbf\u0cc2\u0cc6\u0ccc\u0ccd\u0cd5\u0cd6\u0ce2\u0ce3\u0d3e\u0d41-\u0d44\u0d4d\u0d57\u0d62\u0d63\u0dca\u0dcf\u0dd2-\u0dd4\u0dd6\u0ddf\u0e31\u0e34-\u0e3a\u0e47-\u0e4e\u0eb1\u0eb4-\u0eb9\u0ebb\u0ebc\u0ec8-\u0ecd\u0f18\u0f19\u0f35\u0f37\u0f39\u0f71-\u0f7e\u0f80-\u0f84\u0f86\u0f87\u0f90-\u0f97\u0f99-\u0fbc\u0fc6\u102d-\u1030\u1032-\u1037\u1039\u103a\u103d\u103e\u1058\u1059\u105e-\u1060\u1071-\u1074\u1082\u1085\u1086\u108d\u109d\u135f\u1712-\u1714\u1732-\u1734\u1752\u1753\u1772\u1773\u17b7-\u17bd\u17c6\u17c9-\u17d3\u17dd\u180b-\u180d\u18a9\u1920-\u1922\u1927\u1928\u1932\u1939-\u193b\u1a17\u1a18\u1a56\u1a58-\u1a5e\u1a60\u1a62\u1a65-\u1a6c\u1a73-\u1a7c\u1a7f\u1b00-\u1b03\u1b34\u1b36-\u1b3a\u1b3c\u1b42\u1b6b-\u1b73\u1b80\u1b81\u1ba2-\u1ba5\u1ba8\u1ba9\u1c2c-\u1c33\u1c36\u1c37\u1cd0-\u1cd2\u1cd4-\u1ce0\u1ce2-\u1ce8\u1ced\u1dc0-\u1de6\u1dfd-\u1dff\u200c\u200d\u20d0-\u20f0\u2cef-\u2cf1\u2de0-\u2dff\u302a-\u302f\u3099\u309a\ua66f-\ua672\ua67c\ua67d\ua6f0\ua6f1\ua802\ua806\ua80b\ua825\ua826\ua8c4\ua8e0-\ua8f1\ua926-\ua92d\ua947-\ua951\ua980-\ua982\ua9b3\ua9b6-\ua9b9\ua9bc\uaa29-\uaa2e\uaa31\uaa32\uaa35\uaa36\uaa43\uaa4c\uaab0\uaab2-\uaab4\uaab7\uaab8\uaabe\uaabf\uaac1\uabe5\uabe8\uabed\udc00-\udfff\ufb1e\ufe00-\ufe0f\ufe20-\ufe26\uff9e\uff9f]/;

                function oe(e) {
                    return e.charCodeAt(0) >= 768 && ie.test(e)
                }

                function le(e, t, n) {
                    while ((n < 0 ? t > 0 : t < e.length) && oe(e.charAt(t))) t += n;
                    return t
                }

                function ae(e, t, n) {
                    for (var r = t > n ? -1 : 1;;) {
                        if (t == n) return t;
                        var i = (t + n) / 2,
                            o = r < 0 ? Math.ceil(i) : Math.floor(i);
                        if (o == t) return e(o) ? t : n;
                        e(o) ? n = o : t = o + r
                    }
                }

                function se(e, t, r) {
                    var i = this;
                    this.input = r, i.scrollbarFiller = O("div", null, "CodeMirror-scrollbar-filler"), i.scrollbarFiller.setAttribute("cm-not-content", "true"), i.gutterFiller = O("div", null, "CodeMirror-gutter-filler"), i.gutterFiller.setAttribute("cm-not-content", "true"), i.lineDiv = A("div", null, "CodeMirror-code"), i.selectionDiv = O("div", null, null, "position: relative; z-index: 1"), i.cursorDiv = O("div", null, "CodeMirror-cursors"), i.measure = O("div", null, "CodeMirror-measure"), i.lineMeasure = O("div", null, "CodeMirror-measure"), i.lineSpace = A("div", [i.measure, i.lineMeasure, i.selectionDiv, i.cursorDiv, i.lineDiv], null, "position: relative; outline: none");
                    var o = A("div", [i.lineSpace], "CodeMirror-lines");
                    i.mover = O("div", [o], null, "position: relative"), i.sizer = O("div", [i.mover], "CodeMirror-sizer"), i.sizerWidth = null, i.heightForcer = O("div", null, null, "position: absolute; height: " + $ + "px; width: 1px;"), i.gutters = O("div", null, "CodeMirror-gutters"), i.lineGutter = null, i.scroller = O("div", [i.sizer, i.heightForcer, i.gutters], "CodeMirror-scroll"), i.scroller.setAttribute("tabIndex", "-1"), i.wrapper = O("div", [i.scrollbarFiller, i.gutterFiller, i.scroller], "CodeMirror"), l && a < 8 && (i.gutters.style.zIndex = -1, i.scroller.style.paddingRight = 0), s || n && m || (i.scroller.draggable = !0), e && (e.appendChild ? e.appendChild(i.wrapper) : e(i.wrapper)), i.viewFrom = i.viewTo = t.first, i.reportedViewFrom = i.reportedViewTo = t.first, i.view = [], i.renderedView = null, i.externalMeasured = null, i.viewOffset = 0, i.lastWrapHeight = i.lastWrapWidth = 0, i.updateLineNumbers = null, i.nativeBarWidth = i.barHeight = i.barWidth = 0, i.scrollbarsClipped = !1, i.lineNumWidth = i.lineNumInnerWidth = i.lineNumChars = null, i.alignWidgets = !1, i.cachedCharWidth = i.cachedTextHeight = i.cachedPaddingH = null, i.maxLine = null, i.maxLineLength = 0, i.maxLineChanged = !1, i.wheelDX = i.wheelDY = i.wheelStartX = i.wheelStartY = null, i.shift = !1, i.selForContextMenu = null, i.activeTouch = null, r.init(i)
                }

                function ue(e, t) {
                    if (t -= e.first, t < 0 || t >= e.size) throw new Error("There is no line " + (t + e.first) + " in the document.");
                    var n = e;
                    while (!n.lines)
                        for (var r = 0;; ++r) {
                            var i = n.children[r],
                                o = i.chunkSize();
                            if (t < o) {
                                n = i;
                                break
                            }
                            t -= o
                        }
                    return n.lines[t]
                }

                function ce(e, t, n) {
                    var r = [],
                        i = t.line;
                    return e.iter(t.line, n.line + 1, (function(e) {
                        var o = e.text;
                        i == n.line && (o = o.slice(0, n.ch)), i == t.line && (o = o.slice(t.ch)), r.push(o), ++i
                    })), r
                }

                function fe(e, t, n) {
                    var r = [];
                    return e.iter(t, n, (function(e) {
                        r.push(e.text)
                    })), r
                }

                function he(e, t) {
                    var n = t - e.height;
                    if (n)
                        for (var r = e; r; r = r.parent) r.height += n
                }

                function de(e) {
                    if (null == e.parent) return null;
                    for (var t = e.parent, n = B(t.lines, e), r = t.parent; r; t = r, r = r.parent)
                        for (var i = 0;; ++i) {
                            if (r.children[i] == t) break;
                            n += r.children[i].chunkSize()
                        }
                    return n + t.first
                }

                function pe(e, t) {
                    var n = e.first;
                    e: do {
                        for (var r = 0; r < e.children.length; ++r) {
                            var i = e.children[r],
                                o = i.height;
                            if (t < o) {
                                e = i;
                                continue e
                            }
                            t -= o, n += i.chunkSize()
                        }
                        return n
                    } while (!e.lines);
                    for (var l = 0; l < e.lines.length; ++l) {
                        var a = e.lines[l],
                            s = a.height;
                        if (t < s) break;
                        t -= s
                    }
                    return n + l
                }

                function ge(e, t) {
                    return t >= e.first && t < e.first + e.size
                }

                function ve(e, t) {
                    return String(e.lineNumberFormatter(t + e.firstLineNumber))
                }

                function me(e, t, n) {
                    if (void 0 === n && (n = null), !(this instanceof me)) return new me(e, t, n);
                    this.line = e, this.ch = t, this.sticky = n
                }

                function ye(e, t) {
                    return e.line - t.line || e.ch - t.ch
                }

                function be(e, t) {
                    return e.sticky == t.sticky && 0 == ye(e, t)
                }

                function we(e) {
                    return me(e.line, e.ch)
                }

                function xe(e, t) {
                    return ye(e, t) < 0 ? t : e
                }

                function ke(e, t) {
                    return ye(e, t) < 0 ? e : t
                }

                function Ce(e, t) {
                    return Math.max(e.first, Math.min(t, e.first + e.size - 1))
                }

                function Se(e, t) {
                    if (t.line < e.first) return me(e.first, 0);
                    var n = e.first + e.size - 1;
                    return t.line > n ? me(n, ue(e, n).text.length) : Le(t, ue(e, t.line).text.length)
                }

                function Le(e, t) {
                    var n = e.ch;
                    return null == n || n > t ? me(e.line, t) : n < 0 ? me(e.line, 0) : e
                }

                function Te(e, t) {
                    for (var n = [], r = 0; r < t.length; r++) n[r] = Se(e, t[r]);
                    return n
                }
                var Me = !1,
                    Ne = !1;

                function Oe() {
                    Me = !0
                }

                function Ae() {
                    Ne = !0
                }

                function De(e, t, n) {
                    this.marker = e, this.from = t, this.to = n
                }

                function Ee(e, t) {
                    if (e)
                        for (var n = 0; n < e.length; ++n) {
                            var r = e[n];
                            if (r.marker == t) return r
                        }
                }

                function We(e, t) {
                    for (var n, r = 0; r < e.length; ++r) e[r] != t && (n || (n = [])).push(e[r]);
                    return n
                }

                function He(e, t) {
                    e.markedSpans = e.markedSpans ? e.markedSpans.concat([t]) : [t], t.marker.attachLine(e)
                }

                function Fe(e, t, n) {
                    var r;
                    if (e)
                        for (var i = 0; i < e.length; ++i) {
                            var o = e[i],
                                l = o.marker,
                                a = null == o.from || (l.inclusiveLeft ? o.from <= t : o.from < t);
                            if (a || o.from == t && "bookmark" == l.type && (!n || !o.marker.insertLeft)) {
                                var s = null == o.to || (l.inclusiveRight ? o.to >= t : o.to > t);
                                (r || (r = [])).push(new De(l, o.from, s ? null : o.to))
                            }
                        }
                    return r
                }

                function Ie(e, t, n) {
                    var r;
                    if (e)
                        for (var i = 0; i < e.length; ++i) {
                            var o = e[i],
                                l = o.marker,
                                a = null == o.to || (l.inclusiveRight ? o.to >= t : o.to > t);
                            if (a || o.from == t && "bookmark" == l.type && (!n || o.marker.insertLeft)) {
                                var s = null == o.from || (l.inclusiveLeft ? o.from <= t : o.from < t);
                                (r || (r = [])).push(new De(l, s ? null : o.from - t, null == o.to ? null : o.to - t))
                            }
                        }
                    return r
                }

                function Pe(e, t) {
                    if (t.full) return null;
                    var n = ge(e, t.from.line) && ue(e, t.from.line).markedSpans,
                        r = ge(e, t.to.line) && ue(e, t.to.line).markedSpans;
                    if (!n && !r) return null;
                    var i = t.from.ch,
                        o = t.to.ch,
                        l = 0 == ye(t.from, t.to),
                        a = Fe(n, i, l),
                        s = Ie(r, o, l),
                        u = 1 == t.text.length,
                        c = X(t.text).length + (u ? i : 0);
                    if (a)
                        for (var f = 0; f < a.length; ++f) {
                            var h = a[f];
                            if (null == h.to) {
                                var d = Ee(s, h.marker);
                                d ? u && (h.to = null == d.to ? null : d.to + c) : h.to = i
                            }
                        }
                    if (s)
                        for (var p = 0; p < s.length; ++p) {
                            var g = s[p];
                            if (null != g.to && (g.to += c), null == g.from) {
                                var v = Ee(a, g.marker);
                                v || (g.from = c, u && (a || (a = [])).push(g))
                            } else g.from += c, u && (a || (a = [])).push(g)
                        }
                    a && (a = Re(a)), s && s != a && (s = Re(s));
                    var m = [a];
                    if (!u) {
                        var y, b = t.text.length - 2;
                        if (b > 0 && a)
                            for (var w = 0; w < a.length; ++w) null == a[w].to && (y || (y = [])).push(new De(a[w].marker, null, null));
                        for (var x = 0; x < b; ++x) m.push(y);
                        m.push(s)
                    }
                    return m
                }

                function Re(e) {
                    for (var t = 0; t < e.length; ++t) {
                        var n = e[t];
                        null != n.from && n.from == n.to && !1 !== n.marker.clearWhenEmpty && e.splice(t--, 1)
                    }
                    return e.length ? e : null
                }

                function ze(e, t, n) {
                    var r = null;
                    if (e.iter(t.line, n.line + 1, (function(e) {
                            if (e.markedSpans)
                                for (var t = 0; t < e.markedSpans.length; ++t) {
                                    var n = e.markedSpans[t].marker;
                                    !n.readOnly || r && -1 != B(r, n) || (r || (r = [])).push(n)
                                }
                        })), !r) return null;
                    for (var i = [{
                            from: t,
                            to: n
                        }], o = 0; o < r.length; ++o)
                        for (var l = r[o], a = l.find(0), s = 0; s < i.length; ++s) {
                            var u = i[s];
                            if (!(ye(u.to, a.from) < 0 || ye(u.from, a.to) > 0)) {
                                var c = [s, 1],
                                    f = ye(u.from, a.from),
                                    h = ye(u.to, a.to);
                                (f < 0 || !l.inclusiveLeft && !f) && c.push({
                                    from: u.from,
                                    to: a.from
                                }), (h > 0 || !l.inclusiveRight && !h) && c.push({
                                    from: a.to,
                                    to: u.to
                                }), i.splice.apply(i, c), s += c.length - 3
                            }
                        }
                    return i
                }

                function Be(e) {
                    var t = e.markedSpans;
                    if (t) {
                        for (var n = 0; n < t.length; ++n) t[n].marker.detachLine(e);
                        e.markedSpans = null
                    }
                }

                function $e(e, t) {
                    if (t) {
                        for (var n = 0; n < t.length; ++n) t[n].marker.attachLine(e);
                        e.markedSpans = t
                    }
                }

                function _e(e) {
                    return e.inclusiveLeft ? -1 : 0
                }

                function je(e) {
                    return e.inclusiveRight ? 1 : 0
                }

                function Ge(e, t) {
                    var n = e.lines.length - t.lines.length;
                    if (0 != n) return n;
                    var r = e.find(),
                        i = t.find(),
                        o = ye(r.from, i.from) || _e(e) - _e(t);
                    if (o) return -o;
                    var l = ye(r.to, i.to) || je(e) - je(t);
                    return l || t.id - e.id
                }

                function Ve(e, t) {
                    var n, r = Ne && e.markedSpans;
                    if (r)
                        for (var i = void 0, o = 0; o < r.length; ++o) i = r[o], i.marker.collapsed && null == (t ? i.from : i.to) && (!n || Ge(n, i.marker) < 0) && (n = i.marker);
                    return n
                }

                function Ue(e) {
                    return Ve(e, !0)
                }

                function Ke(e) {
                    return Ve(e, !1)
                }

                function Ye(e, t) {
                    var n, r = Ne && e.markedSpans;
                    if (r)
                        for (var i = 0; i < r.length; ++i) {
                            var o = r[i];
                            o.marker.collapsed && (null == o.from || o.from < t) && (null == o.to || o.to > t) && (!n || Ge(n, o.marker) < 0) && (n = o.marker)
                        }
                    return n
                }

                function Xe(e, t, n, r, i) {
                    var o = ue(e, t),
                        l = Ne && o.markedSpans;
                    if (l)
                        for (var a = 0; a < l.length; ++a) {
                            var s = l[a];
                            if (s.marker.collapsed) {
                                var u = s.marker.find(0),
                                    c = ye(u.from, n) || _e(s.marker) - _e(i),
                                    f = ye(u.to, r) || je(s.marker) - je(i);
                                if (!(c >= 0 && f <= 0 || c <= 0 && f >= 0) && (c <= 0 && (s.marker.inclusiveRight && i.inclusiveLeft ? ye(u.to, n) >= 0 : ye(u.to, n) > 0) || c >= 0 && (s.marker.inclusiveRight && i.inclusiveLeft ? ye(u.from, r) <= 0 : ye(u.from, r) < 0))) return !0
                            }
                        }
                }

                function qe(e) {
                    var t;
                    while (t = Ue(e)) e = t.find(-1, !0).line;
                    return e
                }

                function Je(e) {
                    var t;
                    while (t = Ke(e)) e = t.find(1, !0).line;
                    return e
                }

                function Ze(e) {
                    var t, n;
                    while (t = Ke(e)) e = t.find(1, !0).line, (n || (n = [])).push(e);
                    return n
                }

                function Qe(e, t) {
                    var n = ue(e, t),
                        r = qe(n);
                    return n == r ? t : de(r)
                }

                function et(e, t) {
                    if (t > e.lastLine()) return t;
                    var n, r = ue(e, t);
                    if (!tt(e, r)) return t;
                    while (n = Ke(r)) r = n.find(1, !0).line;
                    return de(r) + 1
                }

                function tt(e, t) {
                    var n = Ne && t.markedSpans;
                    if (n)
                        for (var r = void 0, i = 0; i < n.length; ++i)
                            if (r = n[i], r.marker.collapsed) {
                                if (null == r.from) return !0;
                                if (!r.marker.widgetNode && 0 == r.from && r.marker.inclusiveLeft && nt(e, t, r)) return !0
                            }
                }

                function nt(e, t, n) {
                    if (null == n.to) {
                        var r = n.marker.find(1, !0);
                        return nt(e, r.line, Ee(r.line.markedSpans, n.marker))
                    }
                    if (n.marker.inclusiveRight && n.to == t.text.length) return !0;
                    for (var i = void 0, o = 0; o < t.markedSpans.length; ++o)
                        if (i = t.markedSpans[o], i.marker.collapsed && !i.marker.widgetNode && i.from == n.to && (null == i.to || i.to != n.from) && (i.marker.inclusiveLeft || n.marker.inclusiveRight) && nt(e, t, i)) return !0
                }

                function rt(e) {
                    e = qe(e);
                    for (var t = 0, n = e.parent, r = 0; r < n.lines.length; ++r) {
                        var i = n.lines[r];
                        if (i == e) break;
                        t += i.height
                    }
                    for (var o = n.parent; o; n = o, o = n.parent)
                        for (var l = 0; l < o.children.length; ++l) {
                            var a = o.children[l];
                            if (a == n) break;
                            t += a.height
                        }
                    return t
                }

                function it(e) {
                    if (0 == e.height) return 0;
                    var t, n = e.text.length,
                        r = e;
                    while (t = Ue(r)) {
                        var i = t.find(0, !0);
                        r = i.from.line, n += i.from.ch - i.to.ch
                    }
                    r = e;
                    while (t = Ke(r)) {
                        var o = t.find(0, !0);
                        n -= r.text.length - o.from.ch, r = o.to.line, n += r.text.length - o.to.ch
                    }
                    return n
                }

                function ot(e) {
                    var t = e.display,
                        n = e.doc;
                    t.maxLine = ue(n, n.first), t.maxLineLength = it(t.maxLine), t.maxLineChanged = !0, n.iter((function(e) {
                        var n = it(e);
                        n > t.maxLineLength && (t.maxLineLength = n, t.maxLine = e)
                    }))
                }

                function lt(e, t, n, r) {
                    if (!e) return r(t, n, "ltr", 0);
                    for (var i = !1, o = 0; o < e.length; ++o) {
                        var l = e[o];
                        (l.from < n && l.to > t || t == n && l.to == t) && (r(Math.max(l.from, t), Math.min(l.to, n), 1 == l.level ? "rtl" : "ltr", o), i = !0)
                    }
                    i || r(t, n, "ltr")
                }
                var at = null;

                function st(e, t, n) {
                    var r;
                    at = null;
                    for (var i = 0; i < e.length; ++i) {
                        var o = e[i];
                        if (o.from < t && o.to > t) return i;
                        o.to == t && (o.from != o.to && "before" == n ? r = i : at = i), o.from == t && (o.from != o.to && "before" != n ? r = i : at = i)
                    }
                    return null != r ? r : at
                }
                var ut = function() {
                    var e = "bbbbbbbbbtstwsbbbbbbbbbbbbbbssstwNN%%%NNNNNN,N,N1111111111NNNNNNNLLLLLLLLLLLLLLLLLLLLLLLLLLNNNNNNLLLLLLLLLLLLLLLLLLLLLLLLLLNNNNbbbbbbsbbbbbbbbbbbbbbbbbbbbbbbbbb,N%%%%NNNNLNNNNN%%11NLNNN1LNNNNNLLLLLLLLLLLLLLLLLLLLLLLNLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLN",
                        t = "nnnnnnNNr%%r,rNNmmmmmmmmmmmrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrmmmmmmmmmmmmmmmmmmmmmnnnnnnnnnn%nnrrrmrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrmmmmmmmnNmmmmmmrrmmNmmmmrr1111111111";

                    function n(n) {
                        return n <= 247 ? e.charAt(n) : 1424 <= n && n <= 1524 ? "R" : 1536 <= n && n <= 1785 ? t.charAt(n - 1536) : 1774 <= n && n <= 2220 ? "r" : 8192 <= n && n <= 8203 ? "w" : 8204 == n ? "b" : "L"
                    }
                    var r = /[\u0590-\u05f4\u0600-\u06ff\u0700-\u08ac]/,
                        i = /[stwN]/,
                        o = /[LRr]/,
                        l = /[Lb1n]/,
                        a = /[1n]/;

                    function s(e, t, n) {
                        this.level = e, this.from = t, this.to = n
                    }
                    return function(e, t) {
                        var u = "ltr" == t ? "L" : "R";
                        if (0 == e.length || "ltr" == t && !r.test(e)) return !1;
                        for (var c = e.length, f = [], h = 0; h < c; ++h) f.push(n(e.charCodeAt(h)));
                        for (var d = 0, p = u; d < c; ++d) {
                            var g = f[d];
                            "m" == g ? f[d] = p : p = g
                        }
                        for (var v = 0, m = u; v < c; ++v) {
                            var y = f[v];
                            "1" == y && "r" == m ? f[v] = "n" : o.test(y) && (m = y, "r" == y && (f[v] = "R"))
                        }
                        for (var b = 1, w = f[0]; b < c - 1; ++b) {
                            var x = f[b];
                            "+" == x && "1" == w && "1" == f[b + 1] ? f[b] = "1" : "," != x || w != f[b + 1] || "1" != w && "n" != w || (f[b] = w), w = x
                        }
                        for (var k = 0; k < c; ++k) {
                            var C = f[k];
                            if ("," == C) f[k] = "N";
                            else if ("%" == C) {
                                var S = void 0;
                                for (S = k + 1; S < c && "%" == f[S]; ++S);
                                for (var L = k && "!" == f[k - 1] || S < c && "1" == f[S] ? "1" : "N", T = k; T < S; ++T) f[T] = L;
                                k = S - 1
                            }
                        }
                        for (var M = 0, N = u; M < c; ++M) {
                            var O = f[M];
                            "L" == N && "1" == O ? f[M] = "L" : o.test(O) && (N = O)
                        }
                        for (var A = 0; A < c; ++A)
                            if (i.test(f[A])) {
                                var D = void 0;
                                for (D = A + 1; D < c && i.test(f[D]); ++D);
                                for (var E = "L" == (A ? f[A - 1] : u), W = "L" == (D < c ? f[D] : u), H = E == W ? E ? "L" : "R" : u, F = A; F < D; ++F) f[F] = H;
                                A = D - 1
                            } for (var I, P = [], R = 0; R < c;)
                            if (l.test(f[R])) {
                                var z = R;
                                for (++R; R < c && l.test(f[R]); ++R);
                                P.push(new s(0, z, R))
                            } else {
                                var B = R,
                                    $ = P.length;
                                for (++R; R < c && "L" != f[R]; ++R);
                                for (var _ = B; _ < R;)
                                    if (a.test(f[_])) {
                                        B < _ && P.splice($, 0, new s(1, B, _));
                                        var j = _;
                                        for (++_; _ < R && a.test(f[_]); ++_);
                                        P.splice($, 0, new s(2, j, _)), B = _
                                    } else ++_;
                                B < R && P.splice($, 0, new s(1, B, R))
                            } return "ltr" == t && (1 == P[0].level && (I = e.match(/^\s+/)) && (P[0].from = I[0].length, P.unshift(new s(0, 0, I[0].length))), 1 == X(P).level && (I = e.match(/\s+$/)) && (X(P).to -= I[0].length, P.push(new s(0, c - I[0].length, c)))), "rtl" == t ? P.reverse() : P
                    }
                }();

                function ct(e, t) {
                    var n = e.order;
                    return null == n && (n = e.order = ut(e.text, t)), n
                }
                var ft = [],
                    ht = function(e, t, n) {
                        if (e.addEventListener) e.addEventListener(t, n, !1);
                        else if (e.attachEvent) e.attachEvent("on" + t, n);
                        else {
                            var r = e._handlers || (e._handlers = {});
                            r[t] = (r[t] || ft).concat(n)
                        }
                    };

                function dt(e, t) {
                    return e._handlers && e._handlers[t] || ft
                }

                function pt(e, t, n) {
                    if (e.removeEventListener) e.removeEventListener(t, n, !1);
                    else if (e.detachEvent) e.detachEvent("on" + t, n);
                    else {
                        var r = e._handlers,
                            i = r && r[t];
                        if (i) {
                            var o = B(i, n);
                            o > -1 && (r[t] = i.slice(0, o).concat(i.slice(o + 1)))
                        }
                    }
                }

                function gt(e, t) {
                    var n = dt(e, t);
                    if (n.length)
                        for (var r = Array.prototype.slice.call(arguments, 2), i = 0; i < n.length; ++i) n[i].apply(null, r)
                }

                function vt(e, t, n) {
                    return "string" == typeof t && (t = {
                        type: t,
                        preventDefault: function() {
                            this.defaultPrevented = !0
                        }
                    }), gt(e, n || t.type, e, t), kt(t) || t.codemirrorIgnore
                }

                function mt(e) {
                    var t = e._handlers && e._handlers.cursorActivity;
                    if (t)
                        for (var n = e.curOp.cursorActivityHandlers || (e.curOp.cursorActivityHandlers = []), r = 0; r < t.length; ++r) - 1 == B(n, t[r]) && n.push(t[r])
                }

                function yt(e, t) {
                    return dt(e, t).length > 0
                }

                function bt(e) {
                    e.prototype.on = function(e, t) {
                        ht(this, e, t)
                    }, e.prototype.off = function(e, t) {
                        pt(this, e, t)
                    }
                }

                function wt(e) {
                    e.preventDefault ? e.preventDefault() : e.returnValue = !1
                }

                function xt(e) {
                    e.stopPropagation ? e.stopPropagation() : e.cancelBubble = !0
                }

                function kt(e) {
                    return null != e.defaultPrevented ? e.defaultPrevented : 0 == e.returnValue
                }

                function Ct(e) {
                    wt(e), xt(e)
                }

                function St(e) {
                    return e.target || e.srcElement
                }

                function Lt(e) {
                    var t = e.which;
                    return null == t && (1 & e.button ? t = 1 : 2 & e.button ? t = 3 : 4 & e.button && (t = 2)), y && e.ctrlKey && 1 == t && (t = 3), t
                }
                var Tt, Mt, Nt = function() {
                    if (l && a < 9) return !1;
                    var e = O("div");
                    return "draggable" in e || "dragDrop" in e
                }();

                function Ot(e) {
                    if (null == Tt) {
                        var t = O("span", "​");
                        N(e, O("span", [t, document.createTextNode("x")])), 0 != e.firstChild.offsetHeight && (Tt = t.offsetWidth <= 1 && t.offsetHeight > 2 && !(l && a < 8))
                    }
                    var n = Tt ? O("span", "​") : O("span", " ", null, "display: inline-block; width: 1px; margin-right: -1px");
                    return n.setAttribute("cm-text", ""), n
                }

                function At(e) {
                    if (null != Mt) return Mt;
                    var t = N(e, document.createTextNode("AخA")),
                        n = L(t, 0, 1).getBoundingClientRect(),
                        r = L(t, 1, 2).getBoundingClientRect();
                    return M(e), !(!n || n.left == n.right) && (Mt = r.right - n.right < 3)
                }
                var Dt = 3 != "\n\nb".split(/\n/).length ? function(e) {
                        var t = 0,
                            n = [],
                            r = e.length;
                        while (t <= r) {
                            var i = e.indexOf("\n", t); - 1 == i && (i = e.length);
                            var o = e.slice(t, "\r" == e.charAt(i - 1) ? i - 1 : i),
                                l = o.indexOf("\r"); - 1 != l ? (n.push(o.slice(0, l)), t += l + 1) : (n.push(o), t = i + 1)
                        }
                        return n
                    } : function(e) {
                        return e.split(/\r\n?|\n/)
                    },
                    Et = window.getSelection ? function(e) {
                        try {
                            return e.selectionStart != e.selectionEnd
                        } catch (t) {
                            return !1
                        }
                    } : function(e) {
                        var t;
                        try {
                            t = e.ownerDocument.selection.createRange()
                        } catch (n) {}
                        return !(!t || t.parentElement() != e) && 0 != t.compareEndPoints("StartToEnd", t)
                    },
                    Wt = function() {
                        var e = O("div");
                        return "oncopy" in e || (e.setAttribute("oncopy", "return;"), "function" == typeof e.oncopy)
                    }(),
                    Ht = null;

                function Ft(e) {
                    if (null != Ht) return Ht;
                    var t = N(e, O("span", "x")),
                        n = t.getBoundingClientRect(),
                        r = L(t, 0, 1).getBoundingClientRect();
                    return Ht = Math.abs(n.left - r.left) > 1
                }
                var It = {},
                    Pt = {};

                function Rt(e, t) {
                    arguments.length > 2 && (t.dependencies = Array.prototype.slice.call(arguments, 2)), It[e] = t
                }

                function zt(e, t) {
                    Pt[e] = t
                }

                function Bt(e) {
                    if ("string" == typeof e && Pt.hasOwnProperty(e)) e = Pt[e];
                    else if (e && "string" == typeof e.name && Pt.hasOwnProperty(e.name)) {
                        var t = Pt[e.name];
                        "string" == typeof t && (t = {
                            name: t
                        }), e = Q(t, e), e.name = t.name
                    } else {
                        if ("string" == typeof e && /^[\w\-]+\/[\w\-]+\+xml$/.test(e)) return Bt("application/xml");
                        if ("string" == typeof e && /^[\w\-]+\/[\w\-]+\+json$/.test(e)) return Bt("application/json")
                    }
                    return "string" == typeof e ? {
                        name: e
                    } : e || {
                        name: "null"
                    }
                }

                function $t(e, t) {
                    t = Bt(t);
                    var n = It[t.name];
                    if (!n) return $t(e, "text/plain");
                    var r = n(e, t);
                    if (_t.hasOwnProperty(t.name)) {
                        var i = _t[t.name];
                        for (var o in i) i.hasOwnProperty(o) && (r.hasOwnProperty(o) && (r["_" + o] = r[o]), r[o] = i[o])
                    }
                    if (r.name = t.name, t.helperType && (r.helperType = t.helperType), t.modeProps)
                        for (var l in t.modeProps) r[l] = t.modeProps[l];
                    return r
                }
                var _t = {};

                function jt(e, t) {
                    var n = _t.hasOwnProperty(e) ? _t[e] : _t[e] = {};
                    P(t, n)
                }

                function Gt(e, t) {
                    if (!0 === t) return t;
                    if (e.copyState) return e.copyState(t);
                    var n = {};
                    for (var r in t) {
                        var i = t[r];
                        i instanceof Array && (i = i.concat([])), n[r] = i
                    }
                    return n
                }

                function Vt(e, t) {
                    var n;
                    while (e.innerMode) {
                        if (n = e.innerMode(t), !n || n.mode == e) break;
                        t = n.state, e = n.mode
                    }
                    return n || {
                        mode: e,
                        state: t
                    }
                }

                function Ut(e, t, n) {
                    return !e.startState || e.startState(t, n)
                }
                var Kt = function(e, t, n) {
                    this.pos = this.start = 0, this.string = e, this.tabSize = t || 8, this.lastColumnPos = this.lastColumnValue = 0, this.lineStart = 0, this.lineOracle = n
                };
                Kt.prototype.eol = function() {
                    return this.pos >= this.string.length
                }, Kt.prototype.sol = function() {
                    return this.pos == this.lineStart
                }, Kt.prototype.peek = function() {
                    return this.string.charAt(this.pos) || void 0
                }, Kt.prototype.next = function() {
                    if (this.pos < this.string.length) return this.string.charAt(this.pos++)
                }, Kt.prototype.eat = function(e) {
                    var t, n = this.string.charAt(this.pos);
                    if (t = "string" == typeof e ? n == e : n && (e.test ? e.test(n) : e(n)), t) return ++this.pos, n
                }, Kt.prototype.eatWhile = function(e) {
                    var t = this.pos;
                    while (this.eat(e));
                    return this.pos > t
                }, Kt.prototype.eatSpace = function() {
                    var e = this,
                        t = this.pos;
                    while (/[\s\u00a0]/.test(this.string.charAt(this.pos))) ++e.pos;
                    return this.pos > t
                }, Kt.prototype.skipToEnd = function() {
                    this.pos = this.string.length
                }, Kt.prototype.skipTo = function(e) {
                    var t = this.string.indexOf(e, this.pos);
                    if (t > -1) return this.pos = t, !0
                }, Kt.prototype.backUp = function(e) {
                    this.pos -= e
                }, Kt.prototype.column = function() {
                    return this.lastColumnPos < this.start && (this.lastColumnValue = R(this.string, this.start, this.tabSize, this.lastColumnPos, this.lastColumnValue), this.lastColumnPos = this.start), this.lastColumnValue - (this.lineStart ? R(this.string, this.lineStart, this.tabSize) : 0)
                }, Kt.prototype.indentation = function() {
                    return R(this.string, null, this.tabSize) - (this.lineStart ? R(this.string, this.lineStart, this.tabSize) : 0)
                }, Kt.prototype.match = function(e, t, n) {
                    if ("string" != typeof e) {
                        var r = this.string.slice(this.pos).match(e);
                        return r && r.index > 0 ? null : (r && !1 !== t && (this.pos += r[0].length), r)
                    }
                    var i = function(e) {
                            return n ? e.toLowerCase() : e
                        },
                        o = this.string.substr(this.pos, e.length);
                    if (i(o) == i(e)) return !1 !== t && (this.pos += e.length), !0
                }, Kt.prototype.current = function() {
                    return this.string.slice(this.start, this.pos)
                }, Kt.prototype.hideFirstChars = function(e, t) {
                    this.lineStart += e;
                    try {
                        return t()
                    } finally {
                        this.lineStart -= e
                    }
                }, Kt.prototype.lookAhead = function(e) {
                    var t = this.lineOracle;
                    return t && t.lookAhead(e)
                }, Kt.prototype.baseToken = function() {
                    var e = this.lineOracle;
                    return e && e.baseToken(this.pos)
                };
                var Yt = function(e, t) {
                        this.state = e, this.lookAhead = t
                    },
                    Xt = function(e, t, n, r) {
                        this.state = t, this.doc = e, this.line = n, this.maxLookAhead = r || 0, this.baseTokens = null, this.baseTokenPos = 1
                    };

                function qt(e, t, n, r) {
                    var i = [e.state.modeGen],
                        o = {};
                    ln(e, t.text, e.doc.mode, n, (function(e, t) {
                        return i.push(e, t)
                    }), o, r);
                    for (var l = n.state, a = function(r) {
                            n.baseTokens = i;
                            var a = e.state.overlays[r],
                                s = 1,
                                u = 0;
                            n.state = !0, ln(e, t.text, a.mode, n, (function(e, t) {
                                var n = s;
                                while (u < e) {
                                    var r = i[s];
                                    r > e && i.splice(s, 1, e, i[s + 1], r), s += 2, u = Math.min(e, r)
                                }
                                if (t)
                                    if (a.opaque) i.splice(n, s - n, e, "overlay " + t), s = n + 2;
                                    else
                                        for (; n < s; n += 2) {
                                            var o = i[n + 1];
                                            i[n + 1] = (o ? o + " " : "") + "overlay " + t
                                        }
                            }), o), n.state = l, n.baseTokens = null, n.baseTokenPos = 1
                        }, s = 0; s < e.state.overlays.length; ++s) a(s);
                    return {
                        styles: i,
                        classes: o.bgClass || o.textClass ? o : null
                    }
                }

                function Jt(e, t, n) {
                    if (!t.styles || t.styles[0] != e.state.modeGen) {
                        var r = Zt(e, de(t)),
                            i = t.text.length > e.options.maxHighlightLength && Gt(e.doc.mode, r.state),
                            o = qt(e, t, r);
                        i && (r.state = i), t.stateAfter = r.save(!i), t.styles = o.styles, o.classes ? t.styleClasses = o.classes : t.styleClasses && (t.styleClasses = null), n === e.doc.highlightFrontier && (e.doc.modeFrontier = Math.max(e.doc.modeFrontier, ++e.doc.highlightFrontier))
                    }
                    return t.styles
                }

                function Zt(e, t, n) {
                    var r = e.doc,
                        i = e.display;
                    if (!r.mode.startState) return new Xt(r, !0, t);
                    var o = an(e, t, n),
                        l = o > r.first && ue(r, o - 1).stateAfter,
                        a = l ? Xt.fromSaved(r, l, o) : new Xt(r, Ut(r.mode), o);
                    return r.iter(o, t, (function(n) {
                        Qt(e, n.text, a);
                        var r = a.line;
                        n.stateAfter = r == t - 1 || r % 5 == 0 || r >= i.viewFrom && r < i.viewTo ? a.save() : null, a.nextLine()
                    })), n && (r.modeFrontier = a.line), a
                }

                function Qt(e, t, n, r) {
                    var i = e.doc.mode,
                        o = new Kt(t, e.options.tabSize, n);
                    o.start = o.pos = r || 0, "" == t && en(i, n.state);
                    while (!o.eol()) tn(i, o, n.state), o.start = o.pos
                }

                function en(e, t) {
                    if (e.blankLine) return e.blankLine(t);
                    if (e.innerMode) {
                        var n = Vt(e, t);
                        return n.mode.blankLine ? n.mode.blankLine(n.state) : void 0
                    }
                }

                function tn(e, t, n, r) {
                    for (var i = 0; i < 10; i++) {
                        r && (r[0] = Vt(e, n).mode);
                        var o = e.token(t, n);
                        if (t.pos > t.start) return o
                    }
                    throw new Error("Mode " + e.name + " failed to advance stream.")
                }
                Xt.prototype.lookAhead = function(e) {
                    var t = this.doc.getLine(this.line + e);
                    return null != t && e > this.maxLookAhead && (this.maxLookAhead = e), t
                }, Xt.prototype.baseToken = function(e) {
                    var t = this;
                    if (!this.baseTokens) return null;
                    while (this.baseTokens[this.baseTokenPos] <= e) t.baseTokenPos += 2;
                    var n = this.baseTokens[this.baseTokenPos + 1];
                    return {
                        type: n && n.replace(/( |^)overlay .*/, ""),
                        size: this.baseTokens[this.baseTokenPos] - e
                    }
                }, Xt.prototype.nextLine = function() {
                    this.line++, this.maxLookAhead > 0 && this.maxLookAhead--
                }, Xt.fromSaved = function(e, t, n) {
                    return t instanceof Yt ? new Xt(e, Gt(e.mode, t.state), n, t.lookAhead) : new Xt(e, Gt(e.mode, t), n)
                }, Xt.prototype.save = function(e) {
                    var t = !1 !== e ? Gt(this.doc.mode, this.state) : this.state;
                    return this.maxLookAhead > 0 ? new Yt(t, this.maxLookAhead) : t
                };
                var nn = function(e, t, n) {
                    this.start = e.start, this.end = e.pos, this.string = e.current(), this.type = t || null, this.state = n
                };

                function rn(e, t, n, r) {
                    var i, o = e.doc,
                        l = o.mode;
                    t = Se(o, t);
                    var a, s = ue(o, t.line),
                        u = Zt(e, t.line, n),
                        c = new Kt(s.text, e.options.tabSize, u);
                    r && (a = []);
                    while ((r || c.pos < t.ch) && !c.eol()) c.start = c.pos, i = tn(l, c, u.state), r && a.push(new nn(c, i, Gt(o.mode, u.state)));
                    return r ? a : new nn(c, i, u.state)
                }

                function on(e, t) {
                    if (e)
                        for (;;) {
                            var n = e.match(/(?:^|\s+)line-(background-)?(\S+)/);
                            if (!n) break;
                            e = e.slice(0, n.index) + e.slice(n.index + n[0].length);
                            var r = n[1] ? "bgClass" : "textClass";
                            null == t[r] ? t[r] = n[2] : new RegExp("(?:^|s)" + n[2] + "(?:$|s)").test(t[r]) || (t[r] += " " + n[2])
                        }
                    return e
                }

                function ln(e, t, n, r, i, o, l) {
                    var a = n.flattenSpans;
                    null == a && (a = e.options.flattenSpans);
                    var s, u = 0,
                        c = null,
                        f = new Kt(t, e.options.tabSize, r),
                        h = e.options.addModeClass && [null];
                    "" == t && on(en(n, r.state), o);
                    while (!f.eol()) {
                        if (f.pos > e.options.maxHighlightLength ? (a = !1, l && Qt(e, t, r, f.pos), f.pos = t.length, s = null) : s = on(tn(n, f, r.state, h), o), h) {
                            var d = h[0].name;
                            d && (s = "m-" + (s ? d + " " + s : d))
                        }
                        if (!a || c != s) {
                            while (u < f.start) u = Math.min(f.start, u + 5e3), i(u, c);
                            c = s
                        }
                        f.start = f.pos
                    }
                    while (u < f.pos) {
                        var p = Math.min(f.pos, u + 5e3);
                        i(p, c), u = p
                    }
                }

                function an(e, t, n) {
                    for (var r, i, o = e.doc, l = n ? -1 : t - (e.doc.mode.innerMode ? 1e3 : 100), a = t; a > l; --a) {
                        if (a <= o.first) return o.first;
                        var s = ue(o, a - 1),
                            u = s.stateAfter;
                        if (u && (!n || a + (u instanceof Yt ? u.lookAhead : 0) <= o.modeFrontier)) return a;
                        var c = R(s.text, null, e.options.tabSize);
                        (null == i || r > c) && (i = a - 1, r = c)
                    }
                    return i
                }

                function sn(e, t) {
                    if (e.modeFrontier = Math.min(e.modeFrontier, t), !(e.highlightFrontier < t - 10)) {
                        for (var n = e.first, r = t - 1; r > n; r--) {
                            var i = ue(e, r).stateAfter;
                            if (i && (!(i instanceof Yt) || r + i.lookAhead < t)) {
                                n = r + 1;
                                break
                            }
                        }
                        e.highlightFrontier = Math.min(e.highlightFrontier, n)
                    }
                }
                var un = function(e, t, n) {
                    this.text = e, $e(this, t), this.height = n ? n(this) : 1
                };

                function cn(e, t, n, r) {
                    e.text = t, e.stateAfter && (e.stateAfter = null), e.styles && (e.styles = null), null != e.order && (e.order = null), Be(e), $e(e, n);
                    var i = r ? r(e) : 1;
                    i != e.height && he(e, i)
                }

                function fn(e) {
                    e.parent = null, Be(e)
                }
                un.prototype.lineNo = function() {
                    return de(this)
                }, bt(un);
                var hn = {},
                    dn = {};

                function pn(e, t) {
                    if (!e || /^\s*$/.test(e)) return null;
                    var n = t.addModeClass ? dn : hn;
                    return n[e] || (n[e] = e.replace(/\S+/g, "cm-$&"))
                }

                function gn(e, t) {
                    var n = A("span", null, null, s ? "padding-right: .1px" : null),
                        r = {
                            pre: A("pre", [n], "CodeMirror-line"),
                            content: n,
                            col: 0,
                            pos: 0,
                            cm: e,
                            trailingSpace: !1,
                            splitSpaces: e.getOption("lineWrapping")
                        };
                    t.measure = {};
                    for (var i = 0; i <= (t.rest ? t.rest.length : 0); i++) {
                        var o = i ? t.rest[i - 1] : t.line,
                            l = void 0;
                        r.pos = 0, r.addToken = mn, At(e.display.measure) && (l = ct(o, e.doc.direction)) && (r.addToken = bn(r.addToken, l)), r.map = [];
                        var a = t != e.display.externalMeasured && de(o);
                        xn(o, r, Jt(e, o, a)), o.styleClasses && (o.styleClasses.bgClass && (r.bgClass = H(o.styleClasses.bgClass, r.bgClass || "")), o.styleClasses.textClass && (r.textClass = H(o.styleClasses.textClass, r.textClass || ""))), 0 == r.map.length && r.map.push(0, 0, r.content.appendChild(Ot(e.display.measure))), 0 == i ? (t.measure.map = r.map, t.measure.cache = {}) : ((t.measure.maps || (t.measure.maps = [])).push(r.map), (t.measure.caches || (t.measure.caches = [])).push({}))
                    }
                    if (s) {
                        var u = r.content.lastChild;
                        (/\bcm-tab\b/.test(u.className) || u.querySelector && u.querySelector(".cm-tab")) && (r.content.className = "cm-tab-wrap-hack")
                    }
                    return gt(e, "renderLine", e, t.line, r.pre), r.pre.className && (r.textClass = H(r.pre.className, r.textClass || "")), r
                }

                function vn(e) {
                    var t = O("span", "•", "cm-invalidchar");
                    return t.title = "\\u" + e.charCodeAt(0).toString(16), t.setAttribute("aria-label", t.title), t
                }

                function mn(e, t, n, r, i, o, s) {
                    if (t) {
                        var u, c = e.splitSpaces ? yn(t, e.trailingSpace) : t,
                            f = e.cm.state.specialChars,
                            h = !1;
                        if (f.test(t)) {
                            u = document.createDocumentFragment();
                            var d = 0;
                            while (1) {
                                f.lastIndex = d;
                                var p = f.exec(t),
                                    g = p ? p.index - d : t.length - d;
                                if (g) {
                                    var v = document.createTextNode(c.slice(d, d + g));
                                    l && a < 9 ? u.appendChild(O("span", [v])) : u.appendChild(v), e.map.push(e.pos, e.pos + g, v), e.col += g, e.pos += g
                                }
                                if (!p) break;
                                d += g + 1;
                                var m = void 0;
                                if ("\t" == p[0]) {
                                    var y = e.cm.options.tabSize,
                                        b = y - e.col % y;
                                    m = u.appendChild(O("span", Y(b), "cm-tab")), m.setAttribute("role", "presentation"), m.setAttribute("cm-text", "\t"), e.col += b
                                } else "\r" == p[0] || "\n" == p[0] ? (m = u.appendChild(O("span", "\r" == p[0] ? "␍" : "␤", "cm-invalidchar")), m.setAttribute("cm-text", p[0]), e.col += 1) : (m = e.cm.options.specialCharPlaceholder(p[0]), m.setAttribute("cm-text", p[0]), l && a < 9 ? u.appendChild(O("span", [m])) : u.appendChild(m), e.col += 1);
                                e.map.push(e.pos, e.pos + 1, m), e.pos++
                            }
                        } else e.col += t.length, u = document.createTextNode(c), e.map.push(e.pos, e.pos + t.length, u), l && a < 9 && (h = !0), e.pos += t.length;
                        if (e.trailingSpace = 32 == c.charCodeAt(t.length - 1), n || r || i || h || o) {
                            var w = n || "";
                            r && (w += r), i && (w += i);
                            var x = O("span", [u], w, o);
                            if (s)
                                for (var k in s) s.hasOwnProperty(k) && "style" != k && "class" != k && x.setAttribute(k, s[k]);
                            return e.content.appendChild(x)
                        }
                        e.content.appendChild(u)
                    }
                }

                function yn(e, t) {
                    if (e.length > 1 && !/  /.test(e)) return e;
                    for (var n = t, r = "", i = 0; i < e.length; i++) {
                        var o = e.charAt(i);
                        " " != o || !n || i != e.length - 1 && 32 != e.charCodeAt(i + 1) || (o = " "), r += o, n = " " == o
                    }
                    return r
                }

                function bn(e, t) {
                    return function(n, r, i, o, l, a, s) {
                        i = i ? i + " cm-force-border" : "cm-force-border";
                        for (var u = n.pos, c = u + r.length;;) {
                            for (var f = void 0, h = 0; h < t.length; h++)
                                if (f = t[h], f.to > u && f.from <= u) break;
                            if (f.to >= c) return e(n, r, i, o, l, a, s);
                            e(n, r.slice(0, f.to - u), i, o, null, a, s), o = null, r = r.slice(f.to - u), u = f.to
                        }
                    }
                }

                function wn(e, t, n, r) {
                    var i = !r && n.widgetNode;
                    i && e.map.push(e.pos, e.pos + t, i), !r && e.cm.display.input.needsContentAttribute && (i || (i = e.content.appendChild(document.createElement("span"))), i.setAttribute("cm-marker", n.id)), i && (e.cm.display.input.setUneditable(i), e.content.appendChild(i)), e.pos += t, e.trailingSpace = !1
                }

                function xn(e, t, n) {
                    var r = e.markedSpans,
                        i = e.text,
                        o = 0;
                    if (r)
                        for (var l, a, s, u, c, f, h, d = i.length, p = 0, g = 1, v = "", m = 0;;) {
                            if (m == p) {
                                s = u = c = a = "", h = null, f = null, m = 1 / 0;
                                for (var y = [], b = void 0, w = 0; w < r.length; ++w) {
                                    var x = r[w],
                                        k = x.marker;
                                    if ("bookmark" == k.type && x.from == p && k.widgetNode) y.push(k);
                                    else if (x.from <= p && (null == x.to || x.to > p || k.collapsed && x.to == p && x.from == p)) {
                                        if (null != x.to && x.to != p && m > x.to && (m = x.to, u = ""), k.className && (s += " " + k.className), k.css && (a = (a ? a + ";" : "") + k.css), k.startStyle && x.from == p && (c += " " + k.startStyle), k.endStyle && x.to == m && (b || (b = [])).push(k.endStyle, x.to), k.title && ((h || (h = {})).title = k.title), k.attributes)
                                            for (var C in k.attributes)(h || (h = {}))[C] = k.attributes[C];
                                        k.collapsed && (!f || Ge(f.marker, k) < 0) && (f = x)
                                    } else x.from > p && m > x.from && (m = x.from)
                                }
                                if (b)
                                    for (var S = 0; S < b.length; S += 2) b[S + 1] == m && (u += " " + b[S]);
                                if (!f || f.from == p)
                                    for (var L = 0; L < y.length; ++L) wn(t, 0, y[L]);
                                if (f && (f.from || 0) == p) {
                                    if (wn(t, (null == f.to ? d + 1 : f.to) - p, f.marker, null == f.from), null == f.to) return;
                                    f.to == p && (f = !1)
                                }
                            }
                            if (p >= d) break;
                            var T = Math.min(d, m);
                            while (1) {
                                if (v) {
                                    var M = p + v.length;
                                    if (!f) {
                                        var N = M > T ? v.slice(0, T - p) : v;
                                        t.addToken(t, N, l ? l + s : s, c, p + N.length == m ? u : "", a, h)
                                    }
                                    if (M >= T) {
                                        v = v.slice(T - p), p = T;
                                        break
                                    }
                                    p = M, c = ""
                                }
                                v = i.slice(o, o = n[g++]), l = pn(n[g++], t.cm.options)
                            }
                        } else
                            for (var O = 1; O < n.length; O += 2) t.addToken(t, i.slice(o, o = n[O]), pn(n[O + 1], t.cm.options))
                }

                function kn(e, t, n) {
                    this.line = t, this.rest = Ze(t), this.size = this.rest ? de(X(this.rest)) - n + 1 : 1, this.node = this.text = null, this.hidden = tt(e, t)
                }

                function Cn(e, t, n) {
                    for (var r, i = [], o = t; o < n; o = r) {
                        var l = new kn(e.doc, ue(e.doc, o), o);
                        r = o + l.size, i.push(l)
                    }
                    return i
                }
                var Sn = null;

                function Ln(e) {
                    Sn ? Sn.ops.push(e) : e.ownsGroup = Sn = {
                        ops: [e],
                        delayedCallbacks: []
                    }
                }

                function Tn(e) {
                    var t = e.delayedCallbacks,
                        n = 0;
                    do {
                        for (; n < t.length; n++) t[n].call(null);
                        for (var r = 0; r < e.ops.length; r++) {
                            var i = e.ops[r];
                            if (i.cursorActivityHandlers)
                                while (i.cursorActivityCalled < i.cursorActivityHandlers.length) i.cursorActivityHandlers[i.cursorActivityCalled++].call(null, i.cm)
                        }
                    } while (n < t.length)
                }

                function Mn(e, t) {
                    var n = e.ownsGroup;
                    if (n) try {
                        Tn(n)
                    } finally {
                        Sn = null, t(n)
                    }
                }
                var Nn = null;

                function On(e, t) {
                    var n = dt(e, t);
                    if (n.length) {
                        var r, i = Array.prototype.slice.call(arguments, 2);
                        Sn ? r = Sn.delayedCallbacks : Nn ? r = Nn : (r = Nn = [], setTimeout(An, 0));
                        for (var o = function(e) {
                                r.push((function() {
                                    return n[e].apply(null, i)
                                }))
                            }, l = 0; l < n.length; ++l) o(l)
                    }
                }

                function An() {
                    var e = Nn;
                    Nn = null;
                    for (var t = 0; t < e.length; ++t) e[t]()
                }

                function Dn(e, t, n, r) {
                    for (var i = 0; i < t.changes.length; i++) {
                        var o = t.changes[i];
                        "text" == o ? Fn(e, t) : "gutter" == o ? Pn(e, t, n, r) : "class" == o ? In(e, t) : "widget" == o && Rn(e, t, r)
                    }
                    t.changes = null
                }

                function En(e) {
                    return e.node == e.text && (e.node = O("div", null, null, "position: relative"), e.text.parentNode && e.text.parentNode.replaceChild(e.node, e.text), e.node.appendChild(e.text), l && a < 8 && (e.node.style.zIndex = 2)), e.node
                }

                function Wn(e, t) {
                    var n = t.bgClass ? t.bgClass + " " + (t.line.bgClass || "") : t.line.bgClass;
                    if (n && (n += " CodeMirror-linebackground"), t.background) n ? t.background.className = n : (t.background.parentNode.removeChild(t.background), t.background = null);
                    else if (n) {
                        var r = En(t);
                        t.background = r.insertBefore(O("div", null, n), r.firstChild), e.display.input.setUneditable(t.background)
                    }
                }

                function Hn(e, t) {
                    var n = e.display.externalMeasured;
                    return n && n.line == t.line ? (e.display.externalMeasured = null, t.measure = n.measure, n.built) : gn(e, t)
                }

                function Fn(e, t) {
                    var n = t.text.className,
                        r = Hn(e, t);
                    t.text == t.node && (t.node = r.pre), t.text.parentNode.replaceChild(r.pre, t.text), t.text = r.pre, r.bgClass != t.bgClass || r.textClass != t.textClass ? (t.bgClass = r.bgClass, t.textClass = r.textClass, In(e, t)) : n && (t.text.className = n)
                }

                function In(e, t) {
                    Wn(e, t), t.line.wrapClass ? En(t).className = t.line.wrapClass : t.node != t.text && (t.node.className = "");
                    var n = t.textClass ? t.textClass + " " + (t.line.textClass || "") : t.line.textClass;
                    t.text.className = n || ""
                }

                function Pn(e, t, n, r) {
                    if (t.gutter && (t.node.removeChild(t.gutter), t.gutter = null), t.gutterBackground && (t.node.removeChild(t.gutterBackground), t.gutterBackground = null), t.line.gutterClass) {
                        var i = En(t);
                        t.gutterBackground = O("div", null, "CodeMirror-gutter-background " + t.line.gutterClass, "left: " + (e.options.fixedGutter ? r.fixedPos : -r.gutterTotalWidth) + "px; width: " + r.gutterTotalWidth + "px"), e.display.input.setUneditable(t.gutterBackground), i.insertBefore(t.gutterBackground, t.text)
                    }
                    var o = t.line.gutterMarkers;
                    if (e.options.lineNumbers || o) {
                        var l = En(t),
                            a = t.gutter = O("div", null, "CodeMirror-gutter-wrapper", "left: " + (e.options.fixedGutter ? r.fixedPos : -r.gutterTotalWidth) + "px");
                        if (e.display.input.setUneditable(a), l.insertBefore(a, t.text), t.line.gutterClass && (a.className += " " + t.line.gutterClass), !e.options.lineNumbers || o && o["CodeMirror-linenumbers"] || (t.lineNumber = a.appendChild(O("div", ve(e.options, n), "CodeMirror-linenumber CodeMirror-gutter-elt", "left: " + r.gutterLeft["CodeMirror-linenumbers"] + "px; width: " + e.display.lineNumInnerWidth + "px"))), o)
                            for (var s = 0; s < e.options.gutters.length; ++s) {
                                var u = e.options.gutters[s],
                                    c = o.hasOwnProperty(u) && o[u];
                                c && a.appendChild(O("div", [c], "CodeMirror-gutter-elt", "left: " + r.gutterLeft[u] + "px; width: " + r.gutterWidth[u] + "px"))
                            }
                    }
                }

                function Rn(e, t, n) {
                    t.alignable && (t.alignable = null);
                    for (var r = t.node.firstChild, i = void 0; r; r = i) i = r.nextSibling, "CodeMirror-linewidget" == r.className && t.node.removeChild(r);
                    Bn(e, t, n)
                }

                function zn(e, t, n, r) {
                    var i = Hn(e, t);
                    return t.text = t.node = i.pre, i.bgClass && (t.bgClass = i.bgClass), i.textClass && (t.textClass = i.textClass), In(e, t), Pn(e, t, n, r), Bn(e, t, r), t.node
                }

                function Bn(e, t, n) {
                    if ($n(e, t.line, t, n, !0), t.rest)
                        for (var r = 0; r < t.rest.length; r++) $n(e, t.rest[r], t, n, !1)
                }

                function $n(e, t, n, r, i) {
                    if (t.widgets)
                        for (var o = En(n), l = 0, a = t.widgets; l < a.length; ++l) {
                            var s = a[l],
                                u = O("div", [s.node], "CodeMirror-linewidget");
                            s.handleMouseEvents || u.setAttribute("cm-ignore-events", "true"), _n(s, u, n, r), e.display.input.setUneditable(u), i && s.above ? o.insertBefore(u, n.gutter || n.text) : o.appendChild(u), On(s, "redraw")
                        }
                }

                function _n(e, t, n, r) {
                    if (e.noHScroll) {
                        (n.alignable || (n.alignable = [])).push(t);
                        var i = r.wrapperWidth;
                        t.style.left = r.fixedPos + "px", e.coverGutter || (i -= r.gutterTotalWidth, t.style.paddingLeft = r.gutterTotalWidth + "px"), t.style.width = i + "px"
                    }
                    e.coverGutter && (t.style.zIndex = 5, t.style.position = "relative", e.noHScroll || (t.style.marginLeft = -r.gutterTotalWidth + "px"))
                }

                function jn(e) {
                    if (null != e.height) return e.height;
                    var t = e.doc.cm;
                    if (!t) return 0;
                    if (!D(document.body, e.node)) {
                        var n = "position: relative;";
                        e.coverGutter && (n += "margin-left: -" + t.display.gutters.offsetWidth + "px;"), e.noHScroll && (n += "width: " + t.display.wrapper.clientWidth + "px;"), N(t.display.measure, O("div", [e.node], null, n))
                    }
                    return e.height = e.node.parentNode.offsetHeight
                }

                function Gn(e, t) {
                    for (var n = St(t); n != e.wrapper; n = n.parentNode)
                        if (!n || 1 == n.nodeType && "true" == n.getAttribute("cm-ignore-events") || n.parentNode == e.sizer && n != e.mover) return !0
                }

                function Vn(e) {
                    return e.lineSpace.offsetTop
                }

                function Un(e) {
                    return e.mover.offsetHeight - e.lineSpace.offsetHeight
                }

                function Kn(e) {
                    if (e.cachedPaddingH) return e.cachedPaddingH;
                    var t = N(e.measure, O("pre", "x")),
                        n = window.getComputedStyle ? window.getComputedStyle(t) : t.currentStyle,
                        r = {
                            left: parseInt(n.paddingLeft),
                            right: parseInt(n.paddingRight)
                        };
                    return isNaN(r.left) || isNaN(r.right) || (e.cachedPaddingH = r), r
                }

                function Yn(e) {
                    return $ - e.display.nativeBarWidth
                }

                function Xn(e) {
                    return e.display.scroller.clientWidth - Yn(e) - e.display.barWidth
                }

                function qn(e) {
                    return e.display.scroller.clientHeight - Yn(e) - e.display.barHeight
                }

                function Jn(e, t, n) {
                    var r = e.options.lineWrapping,
                        i = r && Xn(e);
                    if (!t.measure.heights || r && t.measure.width != i) {
                        var o = t.measure.heights = [];
                        if (r) {
                            t.measure.width = i;
                            for (var l = t.text.firstChild.getClientRects(), a = 0; a < l.length - 1; a++) {
                                var s = l[a],
                                    u = l[a + 1];
                                Math.abs(s.bottom - u.bottom) > 2 && o.push((s.bottom + u.top) / 2 - n.top)
                            }
                        }
                        o.push(n.bottom - n.top)
                    }
                }

                function Zn(e, t, n) {
                    if (e.line == t) return {
                        map: e.measure.map,
                        cache: e.measure.cache
                    };
                    for (var r = 0; r < e.rest.length; r++)
                        if (e.rest[r] == t) return {
                            map: e.measure.maps[r],
                            cache: e.measure.caches[r]
                        };
                    for (var i = 0; i < e.rest.length; i++)
                        if (de(e.rest[i]) > n) return {
                            map: e.measure.maps[i],
                            cache: e.measure.caches[i],
                            before: !0
                        }
                }

                function Qn(e, t) {
                    t = qe(t);
                    var n = de(t),
                        r = e.display.externalMeasured = new kn(e.doc, t, n);
                    r.lineN = n;
                    var i = r.built = gn(e, r);
                    return r.text = i.pre, N(e.display.lineMeasure, i.pre), r
                }

                function er(e, t, n, r) {
                    return rr(e, nr(e, t), n, r)
                }

                function tr(e, t) {
                    if (t >= e.display.viewFrom && t < e.display.viewTo) return e.display.view[Ir(e, t)];
                    var n = e.display.externalMeasured;
                    return n && t >= n.lineN && t < n.lineN + n.size ? n : void 0
                }

                function nr(e, t) {
                    var n = de(t),
                        r = tr(e, n);
                    r && !r.text ? r = null : r && r.changes && (Dn(e, r, n, Dr(e)), e.curOp.forceUpdate = !0), r || (r = Qn(e, t));
                    var i = Zn(r, t, n);
                    return {
                        line: t,
                        view: r,
                        rect: null,
                        map: i.map,
                        cache: i.cache,
                        before: i.before,
                        hasHeights: !1
                    }
                }

                function rr(e, t, n, r, i) {
                    t.before && (n = -1);
                    var o, l = n + (r || "");
                    return t.cache.hasOwnProperty(l) ? o = t.cache[l] : (t.rect || (t.rect = t.view.text.getBoundingClientRect()), t.hasHeights || (Jn(e, t.view, t.rect), t.hasHeights = !0), o = sr(e, t, n, r), o.bogus || (t.cache[l] = o)), {
                        left: o.left,
                        right: o.right,
                        top: i ? o.rtop : o.top,
                        bottom: i ? o.rbottom : o.bottom
                    }
                }
                var ir, or = {
                    left: 0,
                    right: 0,
                    top: 0,
                    bottom: 0
                };

                function lr(e, t, n) {
                    for (var r, i, o, l, a, s, u = 0; u < e.length; u += 3)
                        if (a = e[u], s = e[u + 1], t < a ? (i = 0, o = 1, l = "left") : t < s ? (i = t - a, o = i + 1) : (u == e.length - 3 || t == s && e[u + 3] > t) && (o = s - a, i = o - 1, t >= s && (l = "right")), null != i) {
                            if (r = e[u + 2], a == s && n == (r.insertLeft ? "left" : "right") && (l = n), "left" == n && 0 == i)
                                while (u && e[u - 2] == e[u - 3] && e[u - 1].insertLeft) r = e[2 + (u -= 3)], l = "left";
                            if ("right" == n && i == s - a)
                                while (u < e.length - 3 && e[u + 3] == e[u + 4] && !e[u + 5].insertLeft) r = e[(u += 3) + 2], l = "right";
                            break
                        } return {
                        node: r,
                        start: i,
                        end: o,
                        collapse: l,
                        coverStart: a,
                        coverEnd: s
                    }
                }

                function ar(e, t) {
                    var n = or;
                    if ("left" == t) {
                        for (var r = 0; r < e.length; r++)
                            if ((n = e[r]).left != n.right) break
                    } else
                        for (var i = e.length - 1; i >= 0; i--)
                            if ((n = e[i]).left != n.right) break;
                    return n
                }

                function sr(e, t, n, r) {
                    var i, o = lr(t.map, n, r),
                        s = o.node,
                        u = o.start,
                        c = o.end,
                        f = o.collapse;
                    if (3 == s.nodeType) {
                        for (var h = 0; h < 4; h++) {
                            while (u && oe(t.line.text.charAt(o.coverStart + u))) --u;
                            while (o.coverStart + c < o.coverEnd && oe(t.line.text.charAt(o.coverStart + c))) ++c;
                            if (i = l && a < 9 && 0 == u && c == o.coverEnd - o.coverStart ? s.parentNode.getBoundingClientRect() : ar(L(s, u, c).getClientRects(), r), i.left || i.right || 0 == u) break;
                            c = u, u -= 1, f = "right"
                        }
                        l && a < 11 && (i = ur(e.display.measure, i))
                    } else {
                        var d;
                        u > 0 && (f = r = "right"), i = e.options.lineWrapping && (d = s.getClientRects()).length > 1 ? d["right" == r ? d.length - 1 : 0] : s.getBoundingClientRect()
                    }
                    if (l && a < 9 && !u && (!i || !i.left && !i.right)) {
                        var p = s.parentNode.getClientRects()[0];
                        i = p ? {
                            left: p.left,
                            right: p.left + Ar(e.display),
                            top: p.top,
                            bottom: p.bottom
                        } : or
                    }
                    for (var g = i.top - t.rect.top, v = i.bottom - t.rect.top, m = (g + v) / 2, y = t.view.measure.heights, b = 0; b < y.length - 1; b++)
                        if (m < y[b]) break;
                    var w = b ? y[b - 1] : 0,
                        x = y[b],
                        k = {
                            left: ("right" == f ? i.right : i.left) - t.rect.left,
                            right: ("left" == f ? i.left : i.right) - t.rect.left,
                            top: w,
                            bottom: x
                        };
                    return i.left || i.right || (k.bogus = !0), e.options.singleCursorHeightPerLine || (k.rtop = g, k.rbottom = v), k
                }

                function ur(e, t) {
                    if (!window.screen || null == screen.logicalXDPI || screen.logicalXDPI == screen.deviceXDPI || !Ft(e)) return t;
                    var n = screen.logicalXDPI / screen.deviceXDPI,
                        r = screen.logicalYDPI / screen.deviceYDPI;
                    return {
                        left: t.left * n,
                        right: t.right * n,
                        top: t.top * r,
                        bottom: t.bottom * r
                    }
                }

                function cr(e) {
                    if (e.measure && (e.measure.cache = {}, e.measure.heights = null, e.rest))
                        for (var t = 0; t < e.rest.length; t++) e.measure.caches[t] = {}
                }

                function fr(e) {
                    e.display.externalMeasure = null, M(e.display.lineMeasure);
                    for (var t = 0; t < e.display.view.length; t++) cr(e.display.view[t])
                }

                function hr(e) {
                    fr(e), e.display.cachedCharWidth = e.display.cachedTextHeight = e.display.cachedPaddingH = null, e.options.lineWrapping || (e.display.maxLineChanged = !0), e.display.lineNumChars = null
                }

                function dr() {
                    return c && v ? -(document.body.getBoundingClientRect().left - parseInt(getComputedStyle(document.body).marginLeft)) : window.pageXOffset || (document.documentElement || document.body).scrollLeft
                }

                function pr() {
                    return c && v ? -(document.body.getBoundingClientRect().top - parseInt(getComputedStyle(document.body).marginTop)) : window.pageYOffset || (document.documentElement || document.body).scrollTop
                }

                function gr(e) {
                    var t = 0;
                    if (e.widgets)
                        for (var n = 0; n < e.widgets.length; ++n) e.widgets[n].above && (t += jn(e.widgets[n]));
                    return t
                }

                function vr(e, t, n, r, i) {
                    if (!i) {
                        var o = gr(t);
                        n.top += o, n.bottom += o
                    }
                    if ("line" == r) return n;
                    r || (r = "local");
                    var l = rt(t);
                    if ("local" == r ? l += Vn(e.display) : l -= e.display.viewOffset, "page" == r || "window" == r) {
                        var a = e.display.lineSpace.getBoundingClientRect();
                        l += a.top + ("window" == r ? 0 : pr());
                        var s = a.left + ("window" == r ? 0 : dr());
                        n.left += s, n.right += s
                    }
                    return n.top += l, n.bottom += l, n
                }

                function mr(e, t, n) {
                    if ("div" == n) return t;
                    var r = t.left,
                        i = t.top;
                    if ("page" == n) r -= dr(), i -= pr();
                    else if ("local" == n || !n) {
                        var o = e.display.sizer.getBoundingClientRect();
                        r += o.left, i += o.top
                    }
                    var l = e.display.lineSpace.getBoundingClientRect();
                    return {
                        left: r - l.left,
                        top: i - l.top
                    }
                }

                function yr(e, t, n, r, i) {
                    return r || (r = ue(e.doc, t.line)), vr(e, r, er(e, r, t.ch, i), n)
                }

                function br(e, t, n, r, i, o) {
                    function l(t, l) {
                        var a = rr(e, i, t, l ? "right" : "left", o);
                        return l ? a.left = a.right : a.right = a.left, vr(e, r, a, n)
                    }
                    r = r || ue(e.doc, t.line), i || (i = nr(e, r));
                    var a = ct(r, e.doc.direction),
                        s = t.ch,
                        u = t.sticky;
                    if (s >= r.text.length ? (s = r.text.length, u = "before") : s <= 0 && (s = 0, u = "after"), !a) return l("before" == u ? s - 1 : s, "before" == u);

                    function c(e, t, n) {
                        var r = a[t],
                            i = 1 == r.level;
                        return l(n ? e - 1 : e, i != n)
                    }
                    var f = st(a, s, u),
                        h = at,
                        d = c(s, f, "before" == u);
                    return null != h && (d.other = c(s, h, "before" != u)), d
                }

                function wr(e, t) {
                    var n = 0;
                    t = Se(e.doc, t), e.options.lineWrapping || (n = Ar(e.display) * t.ch);
                    var r = ue(e.doc, t.line),
                        i = rt(r) + Vn(e.display);
                    return {
                        left: n,
                        right: n,
                        top: i,
                        bottom: i + r.height
                    }
                }

                function xr(e, t, n, r, i) {
                    var o = me(e, t, n);
                    return o.xRel = i, r && (o.outside = !0), o
                }

                function kr(e, t, n) {
                    var r = e.doc;
                    if (n += e.display.viewOffset, n < 0) return xr(r.first, 0, null, !0, -1);
                    var i = pe(r, n),
                        o = r.first + r.size - 1;
                    if (i > o) return xr(r.first + r.size - 1, ue(r, o).text.length, null, !0, 1);
                    t < 0 && (t = 0);
                    for (var l = ue(r, i);;) {
                        var a = Tr(e, l, i, t, n),
                            s = Ye(l, a.ch + (a.xRel > 0 ? 1 : 0));
                        if (!s) return a;
                        var u = s.find(1);
                        if (u.line == i) return u;
                        l = ue(r, i = u.line)
                    }
                }

                function Cr(e, t, n, r) {
                    r -= gr(t);
                    var i = t.text.length,
                        o = ae((function(t) {
                            return rr(e, n, t - 1).bottom <= r
                        }), i, 0);
                    return i = ae((function(t) {
                        return rr(e, n, t).top > r
                    }), o, i), {
                        begin: o,
                        end: i
                    }
                }

                function Sr(e, t, n, r) {
                    n || (n = nr(e, t));
                    var i = vr(e, t, rr(e, n, r), "line").top;
                    return Cr(e, t, n, i)
                }

                function Lr(e, t, n, r) {
                    return !(e.bottom <= n) && (e.top > n || (r ? e.left : e.right) > t)
                }

                function Tr(e, t, n, r, i) {
                    i -= rt(t);
                    var o = nr(e, t),
                        l = gr(t),
                        a = 0,
                        s = t.text.length,
                        u = !0,
                        c = ct(t, e.doc.direction);
                    if (c) {
                        var f = (e.options.lineWrapping ? Nr : Mr)(e, t, n, o, c, r, i);
                        u = 1 != f.level, a = u ? f.from : f.to - 1, s = u ? f.to : f.from - 1
                    }
                    var h, d, p = null,
                        g = null,
                        v = ae((function(t) {
                            var n = rr(e, o, t);
                            return n.top += l, n.bottom += l, !!Lr(n, r, i, !1) && (n.top <= i && n.left <= r && (p = t, g = n), !0)
                        }), a, s),
                        m = !1;
                    if (g) {
                        var y = r - g.left < g.right - r,
                            b = y == u;
                        v = p + (b ? 0 : 1), d = b ? "after" : "before", h = y ? g.left : g.right
                    } else {
                        u || v != s && v != a || v++, d = 0 == v ? "after" : v == t.text.length ? "before" : rr(e, o, v - (u ? 1 : 0)).bottom + l <= i == u ? "after" : "before";
                        var w = br(e, me(n, v, d), "line", t, o);
                        h = w.left, m = i < w.top || i >= w.bottom
                    }
                    return v = le(t.text, v, 1), xr(n, v, d, m, r - h)
                }

                function Mr(e, t, n, r, i, o, l) {
                    var a = ae((function(a) {
                            var s = i[a],
                                u = 1 != s.level;
                            return Lr(br(e, me(n, u ? s.to : s.from, u ? "before" : "after"), "line", t, r), o, l, !0)
                        }), 0, i.length - 1),
                        s = i[a];
                    if (a > 0) {
                        var u = 1 != s.level,
                            c = br(e, me(n, u ? s.from : s.to, u ? "after" : "before"), "line", t, r);
                        Lr(c, o, l, !0) && c.top > l && (s = i[a - 1])
                    }
                    return s
                }

                function Nr(e, t, n, r, i, o, l) {
                    var a = Cr(e, t, r, l),
                        s = a.begin,
                        u = a.end;
                    /\s/.test(t.text.charAt(u - 1)) && u--;
                    for (var c = null, f = null, h = 0; h < i.length; h++) {
                        var d = i[h];
                        if (!(d.from >= u || d.to <= s)) {
                            var p = 1 != d.level,
                                g = rr(e, r, p ? Math.min(u, d.to) - 1 : Math.max(s, d.from)).right,
                                v = g < o ? o - g + 1e9 : g - o;
                            (!c || f > v) && (c = d, f = v)
                        }
                    }
                    return c || (c = i[i.length - 1]), c.from < s && (c = {
                        from: s,
                        to: c.to,
                        level: c.level
                    }), c.to > u && (c = {
                        from: c.from,
                        to: u,
                        level: c.level
                    }), c
                }

                function Or(e) {
                    if (null != e.cachedTextHeight) return e.cachedTextHeight;
                    if (null == ir) {
                        ir = O("pre");
                        for (var t = 0; t < 49; ++t) ir.appendChild(document.createTextNode("x")), ir.appendChild(O("br"));
                        ir.appendChild(document.createTextNode("x"))
                    }
                    N(e.measure, ir);
                    var n = ir.offsetHeight / 50;
                    return n > 3 && (e.cachedTextHeight = n), M(e.measure), n || 1
                }

                function Ar(e) {
                    if (null != e.cachedCharWidth) return e.cachedCharWidth;
                    var t = O("span", "xxxxxxxxxx"),
                        n = O("pre", [t]);
                    N(e.measure, n);
                    var r = t.getBoundingClientRect(),
                        i = (r.right - r.left) / 10;
                    return i > 2 && (e.cachedCharWidth = i), i || 10
                }

                function Dr(e) {
                    for (var t = e.display, n = {}, r = {}, i = t.gutters.clientLeft, o = t.gutters.firstChild, l = 0; o; o = o.nextSibling, ++l) n[e.options.gutters[l]] = o.offsetLeft + o.clientLeft + i, r[e.options.gutters[l]] = o.clientWidth;
                    return {
                        fixedPos: Er(t),
                        gutterTotalWidth: t.gutters.offsetWidth,
                        gutterLeft: n,
                        gutterWidth: r,
                        wrapperWidth: t.wrapper.clientWidth
                    }
                }

                function Er(e) {
                    return e.scroller.getBoundingClientRect().left - e.sizer.getBoundingClientRect().left
                }

                function Wr(e) {
                    var t = Or(e.display),
                        n = e.options.lineWrapping,
                        r = n && Math.max(5, e.display.scroller.clientWidth / Ar(e.display) - 3);
                    return function(i) {
                        if (tt(e.doc, i)) return 0;
                        var o = 0;
                        if (i.widgets)
                            for (var l = 0; l < i.widgets.length; l++) i.widgets[l].height && (o += i.widgets[l].height);
                        return n ? o + (Math.ceil(i.text.length / r) || 1) * t : o + t
                    }
                }

                function Hr(e) {
                    var t = e.doc,
                        n = Wr(e);
                    t.iter((function(e) {
                        var t = n(e);
                        t != e.height && he(e, t)
                    }))
                }

                function Fr(e, t, n, r) {
                    var i = e.display;
                    if (!n && "true" == St(t).getAttribute("cm-not-content")) return null;
                    var o, l, a = i.lineSpace.getBoundingClientRect();
                    try {
                        o = t.clientX - a.left, l = t.clientY - a.top
                    } catch (t) {
                        return null
                    }
                    var s, u = kr(e, o, l);
                    if (r && 1 == u.xRel && (s = ue(e.doc, u.line).text).length == u.ch) {
                        var c = R(s, s.length, e.options.tabSize) - s.length;
                        u = me(u.line, Math.max(0, Math.round((o - Kn(e.display).left) / Ar(e.display)) - c))
                    }
                    return u
                }

                function Ir(e, t) {
                    if (t >= e.display.viewTo) return null;
                    if (t -= e.display.viewFrom, t < 0) return null;
                    for (var n = e.display.view, r = 0; r < n.length; r++)
                        if (t -= n[r].size, t < 0) return r
                }

                function Pr(e) {
                    e.display.input.showSelection(e.display.input.prepareSelection())
                }

                function Rr(e, t) {
                    void 0 === t && (t = !0);
                    for (var n = e.doc, r = {}, i = r.cursors = document.createDocumentFragment(), o = r.selection = document.createDocumentFragment(), l = 0; l < n.sel.ranges.length; l++)
                        if (t || l != n.sel.primIndex) {
                            var a = n.sel.ranges[l];
                            if (!(a.from().line >= e.display.viewTo || a.to().line < e.display.viewFrom)) {
                                var s = a.empty();
                                (s || e.options.showCursorWhenSelecting) && zr(e, a.head, i), s || $r(e, a, o)
                            }
                        } return r
                }

                function zr(e, t, n) {
                    var r = br(e, t, "div", null, null, !e.options.singleCursorHeightPerLine),
                        i = n.appendChild(O("div", " ", "CodeMirror-cursor"));
                    if (i.style.left = r.left + "px", i.style.top = r.top + "px", i.style.height = Math.max(0, r.bottom - r.top) * e.options.cursorHeight + "px", r.other) {
                        var o = n.appendChild(O("div", " ", "CodeMirror-cursor CodeMirror-secondarycursor"));
                        o.style.display = "", o.style.left = r.other.left + "px", o.style.top = r.other.top + "px", o.style.height = .85 * (r.other.bottom - r.other.top) + "px"
                    }
                }

                function Br(e, t) {
                    return e.top - t.top || e.left - t.left
                }

                function $r(e, t, n) {
                    var r = e.display,
                        i = e.doc,
                        o = document.createDocumentFragment(),
                        l = Kn(e.display),
                        a = l.left,
                        s = Math.max(r.sizerWidth, Xn(e) - r.sizer.offsetLeft) - l.right,
                        u = "ltr" == i.direction;

                    function c(e, t, n, r) {
                        t < 0 && (t = 0), t = Math.round(t), r = Math.round(r), o.appendChild(O("div", null, "CodeMirror-selected", "position: absolute; left: " + e + "px;\n                             top: " + t + "px; width: " + (null == n ? s - e : n) + "px;\n                             height: " + (r - t) + "px"))
                    }

                    function f(t, n, r) {
                        var o, l, f = ue(i, t),
                            h = f.text.length;

                        function d(n, r) {
                            return yr(e, me(t, n), "div", f, r)
                        }

                        function p(t, n, r) {
                            var i = Sr(e, f, null, t),
                                o = "ltr" == n == ("after" == r) ? "left" : "right",
                                l = "after" == r ? i.begin : i.end - (/\s/.test(f.text.charAt(i.end - 1)) ? 2 : 1);
                            return d(l, o)[o]
                        }
                        var g = ct(f, i.direction);
                        return lt(g, n || 0, null == r ? h : r, (function(e, t, i, f) {
                            var v = "ltr" == i,
                                m = d(e, v ? "left" : "right"),
                                y = d(t - 1, v ? "right" : "left"),
                                b = null == n && 0 == e,
                                w = null == r && t == h,
                                x = 0 == f,
                                k = !g || f == g.length - 1;
                            if (y.top - m.top <= 3) {
                                var C = (u ? b : w) && x,
                                    S = (u ? w : b) && k,
                                    L = C ? a : (v ? m : y).left,
                                    T = S ? s : (v ? y : m).right;
                                c(L, m.top, T - L, m.bottom)
                            } else {
                                var M, N, O, A;
                                v ? (M = u && b && x ? a : m.left, N = u ? s : p(e, i, "before"), O = u ? a : p(t, i, "after"), A = u && w && k ? s : y.right) : (M = u ? p(e, i, "before") : a, N = !u && b && x ? s : m.right, O = !u && w && k ? a : y.left, A = u ? p(t, i, "after") : s), c(M, m.top, N - M, m.bottom), m.bottom < y.top && c(a, m.bottom, null, y.top), c(O, y.top, A - O, y.bottom)
                            }(!o || Br(m, o) < 0) && (o = m), Br(y, o) < 0 && (o = y), (!l || Br(m, l) < 0) && (l = m), Br(y, l) < 0 && (l = y)
                        })), {
                            start: o,
                            end: l
                        }
                    }
                    var h = t.from(),
                        d = t.to();
                    if (h.line == d.line) f(h.line, h.ch, d.ch);
                    else {
                        var p = ue(i, h.line),
                            g = ue(i, d.line),
                            v = qe(p) == qe(g),
                            m = f(h.line, h.ch, v ? p.text.length + 1 : null).end,
                            y = f(d.line, v ? 0 : null, d.ch).start;
                        v && (m.top < y.top - 2 ? (c(m.right, m.top, null, m.bottom), c(a, y.top, y.left, y.bottom)) : c(m.right, m.top, y.left - m.right, m.bottom)), m.bottom < y.top && c(a, m.bottom, null, y.top)
                    }
                    n.appendChild(o)
                }

                function _r(e) {
                    if (e.state.focused) {
                        var t = e.display;
                        clearInterval(t.blinker);
                        var n = !0;
                        t.cursorDiv.style.visibility = "", e.options.cursorBlinkRate > 0 ? t.blinker = setInterval((function() {
                            return t.cursorDiv.style.visibility = (n = !n) ? "" : "hidden"
                        }), e.options.cursorBlinkRate) : e.options.cursorBlinkRate < 0 && (t.cursorDiv.style.visibility = "hidden")
                    }
                }

                function jr(e) {
                    e.state.focused || (e.display.input.focus(), Vr(e))
                }

                function Gr(e) {
                    e.state.delayingBlurEvent = !0, setTimeout((function() {
                        e.state.delayingBlurEvent && (e.state.delayingBlurEvent = !1, Ur(e))
                    }), 100)
                }

                function Vr(e, t) {
                    e.state.delayingBlurEvent && (e.state.delayingBlurEvent = !1), "nocursor" != e.options.readOnly && (e.state.focused || (gt(e, "focus", e, t), e.state.focused = !0, W(e.display.wrapper, "CodeMirror-focused"), e.curOp || e.display.selForContextMenu == e.doc.sel || (e.display.input.reset(), s && setTimeout((function() {
                        return e.display.input.reset(!0)
                    }), 20)), e.display.input.receivedFocus()), _r(e))
                }

                function Ur(e, t) {
                    e.state.delayingBlurEvent || (e.state.focused && (gt(e, "blur", e, t), e.state.focused = !1, T(e.display.wrapper, "CodeMirror-focused")), clearInterval(e.display.blinker), setTimeout((function() {
                        e.state.focused || (e.display.shift = !1)
                    }), 150))
                }

                function Kr(e) {
                    for (var t = e.display, n = t.lineDiv.offsetTop, r = 0; r < t.view.length; r++) {
                        var i = t.view[r],
                            o = e.options.lineWrapping,
                            s = void 0,
                            u = 0;
                        if (!i.hidden) {
                            if (l && a < 8) {
                                var c = i.node.offsetTop + i.node.offsetHeight;
                                s = c - n, n = c
                            } else {
                                var f = i.node.getBoundingClientRect();
                                s = f.bottom - f.top, !o && i.text.firstChild && (u = i.text.firstChild.getBoundingClientRect().right - f.left - 1)
                            }
                            var h = i.line.height - s;
                            if ((h > .005 || h < -.005) && (he(i.line, s), Yr(i.line), i.rest))
                                for (var d = 0; d < i.rest.length; d++) Yr(i.rest[d]);
                            if (u > e.display.sizerWidth) {
                                var p = Math.ceil(u / Ar(e.display));
                                p > e.display.maxLineLength && (e.display.maxLineLength = p, e.display.maxLine = i.line, e.display.maxLineChanged = !0)
                            }
                        }
                    }
                }

                function Yr(e) {
                    if (e.widgets)
                        for (var t = 0; t < e.widgets.length; ++t) {
                            var n = e.widgets[t],
                                r = n.node.parentNode;
                            r && (n.height = r.offsetHeight)
                        }
                }

                function Xr(e, t, n) {
                    var r = n && null != n.top ? Math.max(0, n.top) : e.scroller.scrollTop;
                    r = Math.floor(r - Vn(e));
                    var i = n && null != n.bottom ? n.bottom : r + e.wrapper.clientHeight,
                        o = pe(t, r),
                        l = pe(t, i);
                    if (n && n.ensure) {
                        var a = n.ensure.from.line,
                            s = n.ensure.to.line;
                        a < o ? (o = a, l = pe(t, rt(ue(t, a)) + e.wrapper.clientHeight)) : Math.min(s, t.lastLine()) >= l && (o = pe(t, rt(ue(t, s)) - e.wrapper.clientHeight), l = s)
                    }
                    return {
                        from: o,
                        to: Math.max(l, o + 1)
                    }
                }

                function qr(e) {
                    var t = e.display,
                        n = t.view;
                    if (t.alignWidgets || t.gutters.firstChild && e.options.fixedGutter) {
                        for (var r = Er(t) - t.scroller.scrollLeft + e.doc.scrollLeft, i = t.gutters.offsetWidth, o = r + "px", l = 0; l < n.length; l++)
                            if (!n[l].hidden) {
                                e.options.fixedGutter && (n[l].gutter && (n[l].gutter.style.left = o), n[l].gutterBackground && (n[l].gutterBackground.style.left = o));
                                var a = n[l].alignable;
                                if (a)
                                    for (var s = 0; s < a.length; s++) a[s].style.left = o
                            } e.options.fixedGutter && (t.gutters.style.left = r + i + "px")
                    }
                }

                function Jr(e) {
                    if (!e.options.lineNumbers) return !1;
                    var t = e.doc,
                        n = ve(e.options, t.first + t.size - 1),
                        r = e.display;
                    if (n.length != r.lineNumChars) {
                        var i = r.measure.appendChild(O("div", [O("div", n)], "CodeMirror-linenumber CodeMirror-gutter-elt")),
                            o = i.firstChild.offsetWidth,
                            l = i.offsetWidth - o;
                        return r.lineGutter.style.width = "", r.lineNumInnerWidth = Math.max(o, r.lineGutter.offsetWidth - l) + 1, r.lineNumWidth = r.lineNumInnerWidth + l, r.lineNumChars = r.lineNumInnerWidth ? n.length : -1, r.lineGutter.style.width = r.lineNumWidth + "px", Ki(e), !0
                    }
                    return !1
                }

                function Zr(e, t) {
                    if (!vt(e, "scrollCursorIntoView")) {
                        var n = e.display,
                            r = n.sizer.getBoundingClientRect(),
                            i = null;
                        if (t.top + r.top < 0 ? i = !0 : t.bottom + r.top > (window.innerHeight || document.documentElement.clientHeight) && (i = !1), null != i && !p) {
                            var o = O("div", "​", null, "position: absolute;\n                         top: " + (t.top - n.viewOffset - Vn(e.display)) + "px;\n                         height: " + (t.bottom - t.top + Yn(e) + n.barHeight) + "px;\n                         left: " + t.left + "px; width: " + Math.max(2, t.right - t.left) + "px;");
                            e.display.lineSpace.appendChild(o), o.scrollIntoView(i), e.display.lineSpace.removeChild(o)
                        }
                    }
                }

                function Qr(e, t, n, r) {
                    var i;
                    null == r && (r = 0), e.options.lineWrapping || t != n || (t = t.ch ? me(t.line, "before" == t.sticky ? t.ch - 1 : t.ch, "after") : t, n = "before" == t.sticky ? me(t.line, t.ch + 1, "before") : t);
                    for (var o = 0; o < 5; o++) {
                        var l = !1,
                            a = br(e, t),
                            s = n && n != t ? br(e, n) : a;
                        i = {
                            left: Math.min(a.left, s.left),
                            top: Math.min(a.top, s.top) - r,
                            right: Math.max(a.left, s.left),
                            bottom: Math.max(a.bottom, s.bottom) + r
                        };
                        var u = ti(e, i),
                            c = e.doc.scrollTop,
                            f = e.doc.scrollLeft;
                        if (null != u.scrollTop && (si(e, u.scrollTop), Math.abs(e.doc.scrollTop - c) > 1 && (l = !0)), null != u.scrollLeft && (ci(e, u.scrollLeft), Math.abs(e.doc.scrollLeft - f) > 1 && (l = !0)), !l) break
                    }
                    return i
                }

                function ei(e, t) {
                    var n = ti(e, t);
                    null != n.scrollTop && si(e, n.scrollTop), null != n.scrollLeft && ci(e, n.scrollLeft)
                }

                function ti(e, t) {
                    var n = e.display,
                        r = Or(e.display);
                    t.top < 0 && (t.top = 0);
                    var i = e.curOp && null != e.curOp.scrollTop ? e.curOp.scrollTop : n.scroller.scrollTop,
                        o = qn(e),
                        l = {};
                    t.bottom - t.top > o && (t.bottom = t.top + o);
                    var a = e.doc.height + Un(n),
                        s = t.top < r,
                        u = t.bottom > a - r;
                    if (t.top < i) l.scrollTop = s ? 0 : t.top;
                    else if (t.bottom > i + o) {
                        var c = Math.min(t.top, (u ? a : t.bottom) - o);
                        c != i && (l.scrollTop = c)
                    }
                    var f = e.curOp && null != e.curOp.scrollLeft ? e.curOp.scrollLeft : n.scroller.scrollLeft,
                        h = Xn(e) - (e.options.fixedGutter ? n.gutters.offsetWidth : 0),
                        d = t.right - t.left > h;
                    return d && (t.right = t.left + h), t.left < 10 ? l.scrollLeft = 0 : t.left < f ? l.scrollLeft = Math.max(0, t.left - (d ? 0 : 10)) : t.right > h + f - 3 && (l.scrollLeft = t.right + (d ? 0 : 10) - h), l
                }

                function ni(e, t) {
                    null != t && (li(e), e.curOp.scrollTop = (null == e.curOp.scrollTop ? e.doc.scrollTop : e.curOp.scrollTop) + t)
                }

                function ri(e) {
                    li(e);
                    var t = e.getCursor();
                    e.curOp.scrollToPos = {
                        from: t,
                        to: t,
                        margin: e.options.cursorScrollMargin
                    }
                }

                function ii(e, t, n) {
                    null == t && null == n || li(e), null != t && (e.curOp.scrollLeft = t), null != n && (e.curOp.scrollTop = n)
                }

                function oi(e, t) {
                    li(e), e.curOp.scrollToPos = t
                }

                function li(e) {
                    var t = e.curOp.scrollToPos;
                    if (t) {
                        e.curOp.scrollToPos = null;
                        var n = wr(e, t.from),
                            r = wr(e, t.to);
                        ai(e, n, r, t.margin)
                    }
                }

                function ai(e, t, n, r) {
                    var i = ti(e, {
                        left: Math.min(t.left, n.left),
                        top: Math.min(t.top, n.top) - r,
                        right: Math.max(t.right, n.right),
                        bottom: Math.max(t.bottom, n.bottom) + r
                    });
                    ii(e, i.scrollLeft, i.scrollTop)
                }

                function si(e, t) {
                    Math.abs(e.doc.scrollTop - t) < 2 || (n || Vi(e, {
                        top: t
                    }), ui(e, t, !0), n && Vi(e), Pi(e, 100))
                }

                function ui(e, t, n) {
                    t = Math.min(e.display.scroller.scrollHeight - e.display.scroller.clientHeight, t), (e.display.scroller.scrollTop != t || n) && (e.doc.scrollTop = t, e.display.scrollbars.setScrollTop(t), e.display.scroller.scrollTop != t && (e.display.scroller.scrollTop = t))
                }

                function ci(e, t, n, r) {
                    t = Math.min(t, e.display.scroller.scrollWidth - e.display.scroller.clientWidth), (n ? t == e.doc.scrollLeft : Math.abs(e.doc.scrollLeft - t) < 2) && !r || (e.doc.scrollLeft = t, qr(e), e.display.scroller.scrollLeft != t && (e.display.scroller.scrollLeft = t), e.display.scrollbars.setScrollLeft(t))
                }

                function fi(e) {
                    var t = e.display,
                        n = t.gutters.offsetWidth,
                        r = Math.round(e.doc.height + Un(e.display));
                    return {
                        clientHeight: t.scroller.clientHeight,
                        viewHeight: t.wrapper.clientHeight,
                        scrollWidth: t.scroller.scrollWidth,
                        clientWidth: t.scroller.clientWidth,
                        viewWidth: t.wrapper.clientWidth,
                        barLeft: e.options.fixedGutter ? n : 0,
                        docHeight: r,
                        scrollHeight: r + Yn(e) + t.barHeight,
                        nativeBarWidth: t.nativeBarWidth,
                        gutterWidth: n
                    }
                }
                var hi = function(e, t, n) {
                    this.cm = n;
                    var r = this.vert = O("div", [O("div", null, null, "min-width: 1px")], "CodeMirror-vscrollbar"),
                        i = this.horiz = O("div", [O("div", null, null, "height: 100%; min-height: 1px")], "CodeMirror-hscrollbar");
                    r.tabIndex = i.tabIndex = -1, e(r), e(i), ht(r, "scroll", (function() {
                        r.clientHeight && t(r.scrollTop, "vertical")
                    })), ht(i, "scroll", (function() {
                        i.clientWidth && t(i.scrollLeft, "horizontal")
                    })), this.checkedZeroWidth = !1, l && a < 8 && (this.horiz.style.minHeight = this.vert.style.minWidth = "18px")
                };
                hi.prototype.update = function(e) {
                    var t = e.scrollWidth > e.clientWidth + 1,
                        n = e.scrollHeight > e.clientHeight + 1,
                        r = e.nativeBarWidth;
                    if (n) {
                        this.vert.style.display = "block", this.vert.style.bottom = t ? r + "px" : "0";
                        var i = e.viewHeight - (t ? r : 0);
                        this.vert.firstChild.style.height = Math.max(0, e.scrollHeight - e.clientHeight + i) + "px"
                    } else this.vert.style.display = "", this.vert.firstChild.style.height = "0";
                    if (t) {
                        this.horiz.style.display = "block", this.horiz.style.right = n ? r + "px" : "0", this.horiz.style.left = e.barLeft + "px";
                        var o = e.viewWidth - e.barLeft - (n ? r : 0);
                        this.horiz.firstChild.style.width = Math.max(0, e.scrollWidth - e.clientWidth + o) + "px"
                    } else this.horiz.style.display = "", this.horiz.firstChild.style.width = "0";
                    return !this.checkedZeroWidth && e.clientHeight > 0 && (0 == r && this.zeroWidthHack(), this.checkedZeroWidth = !0), {
                        right: n ? r : 0,
                        bottom: t ? r : 0
                    }
                }, hi.prototype.setScrollLeft = function(e) {
                    this.horiz.scrollLeft != e && (this.horiz.scrollLeft = e), this.disableHoriz && this.enableZeroWidthBar(this.horiz, this.disableHoriz, "horiz")
                }, hi.prototype.setScrollTop = function(e) {
                    this.vert.scrollTop != e && (this.vert.scrollTop = e), this.disableVert && this.enableZeroWidthBar(this.vert, this.disableVert, "vert")
                }, hi.prototype.zeroWidthHack = function() {
                    var e = y && !d ? "12px" : "18px";
                    this.horiz.style.height = this.vert.style.width = e, this.horiz.style.pointerEvents = this.vert.style.pointerEvents = "none", this.disableHoriz = new z, this.disableVert = new z
                }, hi.prototype.enableZeroWidthBar = function(e, t, n) {
                    function r() {
                        var i = e.getBoundingClientRect(),
                            o = "vert" == n ? document.elementFromPoint(i.right - 1, (i.top + i.bottom) / 2) : document.elementFromPoint((i.right + i.left) / 2, i.bottom - 1);
                        o != e ? e.style.pointerEvents = "none" : t.set(1e3, r)
                    }
                    e.style.pointerEvents = "auto", t.set(1e3, r)
                }, hi.prototype.clear = function() {
                    var e = this.horiz.parentNode;
                    e.removeChild(this.horiz), e.removeChild(this.vert)
                };
                var di = function() {};

                function pi(e, t) {
                    t || (t = fi(e));
                    var n = e.display.barWidth,
                        r = e.display.barHeight;
                    gi(e, t);
                    for (var i = 0; i < 4 && n != e.display.barWidth || r != e.display.barHeight; i++) n != e.display.barWidth && e.options.lineWrapping && Kr(e), gi(e, fi(e)), n = e.display.barWidth, r = e.display.barHeight
                }

                function gi(e, t) {
                    var n = e.display,
                        r = n.scrollbars.update(t);
                    n.sizer.style.paddingRight = (n.barWidth = r.right) + "px", n.sizer.style.paddingBottom = (n.barHeight = r.bottom) + "px", n.heightForcer.style.borderBottom = r.bottom + "px solid transparent", r.right && r.bottom ? (n.scrollbarFiller.style.display = "block", n.scrollbarFiller.style.height = r.bottom + "px", n.scrollbarFiller.style.width = r.right + "px") : n.scrollbarFiller.style.display = "", r.bottom && e.options.coverGutterNextToScrollbar && e.options.fixedGutter ? (n.gutterFiller.style.display = "block", n.gutterFiller.style.height = r.bottom + "px", n.gutterFiller.style.width = t.gutterWidth + "px") : n.gutterFiller.style.display = ""
                }
                di.prototype.update = function() {
                    return {
                        bottom: 0,
                        right: 0
                    }
                }, di.prototype.setScrollLeft = function() {}, di.prototype.setScrollTop = function() {}, di.prototype.clear = function() {};
                var vi = {
                    native: hi,
                    null: di
                };

                function mi(e) {
                    e.display.scrollbars && (e.display.scrollbars.clear(), e.display.scrollbars.addClass && T(e.display.wrapper, e.display.scrollbars.addClass)), e.display.scrollbars = new vi[e.options.scrollbarStyle]((function(t) {
                        e.display.wrapper.insertBefore(t, e.display.scrollbarFiller), ht(t, "mousedown", (function() {
                            e.state.focused && setTimeout((function() {
                                return e.display.input.focus()
                            }), 0)
                        })), t.setAttribute("cm-not-content", "true")
                    }), (function(t, n) {
                        "horizontal" == n ? ci(e, t) : si(e, t)
                    }), e), e.display.scrollbars.addClass && W(e.display.wrapper, e.display.scrollbars.addClass)
                }
                var yi = 0;

                function bi(e) {
                    e.curOp = {
                        cm: e,
                        viewChanged: !1,
                        startHeight: e.doc.height,
                        forceUpdate: !1,
                        updateInput: 0,
                        typing: !1,
                        changeObjs: null,
                        cursorActivityHandlers: null,
                        cursorActivityCalled: 0,
                        selectionChanged: !1,
                        updateMaxLine: !1,
                        scrollLeft: null,
                        scrollTop: null,
                        scrollToPos: null,
                        focus: !1,
                        id: ++yi
                    }, Ln(e.curOp)
                }

                function wi(e) {
                    var t = e.curOp;
                    t && Mn(t, (function(e) {
                        for (var t = 0; t < e.ops.length; t++) e.ops[t].cm.curOp = null;
                        xi(e)
                    }))
                }

                function xi(e) {
                    for (var t = e.ops, n = 0; n < t.length; n++) ki(t[n]);
                    for (var r = 0; r < t.length; r++) Ci(t[r]);
                    for (var i = 0; i < t.length; i++) Si(t[i]);
                    for (var o = 0; o < t.length; o++) Li(t[o]);
                    for (var l = 0; l < t.length; l++) Ti(t[l])
                }

                function ki(e) {
                    var t = e.cm,
                        n = t.display;
                    Bi(t), e.updateMaxLine && ot(t), e.mustUpdate = e.viewChanged || e.forceUpdate || null != e.scrollTop || e.scrollToPos && (e.scrollToPos.from.line < n.viewFrom || e.scrollToPos.to.line >= n.viewTo) || n.maxLineChanged && t.options.lineWrapping, e.update = e.mustUpdate && new zi(t, e.mustUpdate && {
                        top: e.scrollTop,
                        ensure: e.scrollToPos
                    }, e.forceUpdate)
                }

                function Ci(e) {
                    e.updatedDisplay = e.mustUpdate && ji(e.cm, e.update)
                }

                function Si(e) {
                    var t = e.cm,
                        n = t.display;
                    e.updatedDisplay && Kr(t), e.barMeasure = fi(t), n.maxLineChanged && !t.options.lineWrapping && (e.adjustWidthTo = er(t, n.maxLine, n.maxLine.text.length).left + 3, t.display.sizerWidth = e.adjustWidthTo, e.barMeasure.scrollWidth = Math.max(n.scroller.clientWidth, n.sizer.offsetLeft + e.adjustWidthTo + Yn(t) + t.display.barWidth), e.maxScrollLeft = Math.max(0, n.sizer.offsetLeft + e.adjustWidthTo - Xn(t))), (e.updatedDisplay || e.selectionChanged) && (e.preparedSelection = n.input.prepareSelection())
                }

                function Li(e) {
                    var t = e.cm;
                    null != e.adjustWidthTo && (t.display.sizer.style.minWidth = e.adjustWidthTo + "px", e.maxScrollLeft < t.doc.scrollLeft && ci(t, Math.min(t.display.scroller.scrollLeft, e.maxScrollLeft), !0), t.display.maxLineChanged = !1);
                    var n = e.focus && e.focus == E();
                    e.preparedSelection && t.display.input.showSelection(e.preparedSelection, n), (e.updatedDisplay || e.startHeight != t.doc.height) && pi(t, e.barMeasure), e.updatedDisplay && Yi(t, e.barMeasure), e.selectionChanged && _r(t), t.state.focused && e.updateInput && t.display.input.reset(e.typing), n && jr(e.cm)
                }

                function Ti(e) {
                    var t = e.cm,
                        n = t.display,
                        r = t.doc;
                    if (e.updatedDisplay && Gi(t, e.update), null == n.wheelStartX || null == e.scrollTop && null == e.scrollLeft && !e.scrollToPos || (n.wheelStartX = n.wheelStartY = null), null != e.scrollTop && ui(t, e.scrollTop, e.forceScroll), null != e.scrollLeft && ci(t, e.scrollLeft, !0, !0), e.scrollToPos) {
                        var i = Qr(t, Se(r, e.scrollToPos.from), Se(r, e.scrollToPos.to), e.scrollToPos.margin);
                        Zr(t, i)
                    }
                    var o = e.maybeHiddenMarkers,
                        l = e.maybeUnhiddenMarkers;
                    if (o)
                        for (var a = 0; a < o.length; ++a) o[a].lines.length || gt(o[a], "hide");
                    if (l)
                        for (var s = 0; s < l.length; ++s) l[s].lines.length && gt(l[s], "unhide");
                    n.wrapper.offsetHeight && (r.scrollTop = t.display.scroller.scrollTop), e.changeObjs && gt(t, "changes", t, e.changeObjs), e.update && e.update.finish()
                }

                function Mi(e, t) {
                    if (e.curOp) return t();
                    bi(e);
                    try {
                        return t()
                    } finally {
                        wi(e)
                    }
                }

                function Ni(e, t) {
                    return function() {
                        if (e.curOp) return t.apply(e, arguments);
                        bi(e);
                        try {
                            return t.apply(e, arguments)
                        } finally {
                            wi(e)
                        }
                    }
                }

                function Oi(e) {
                    return function() {
                        if (this.curOp) return e.apply(this, arguments);
                        bi(this);
                        try {
                            return e.apply(this, arguments)
                        } finally {
                            wi(this)
                        }
                    }
                }

                function Ai(e) {
                    return function() {
                        var t = this.cm;
                        if (!t || t.curOp) return e.apply(this, arguments);
                        bi(t);
                        try {
                            return e.apply(this, arguments)
                        } finally {
                            wi(t)
                        }
                    }
                }

                function Di(e, t, n, r) {
                    null == t && (t = e.doc.first), null == n && (n = e.doc.first + e.doc.size), r || (r = 0);
                    var i = e.display;
                    if (r && n < i.viewTo && (null == i.updateLineNumbers || i.updateLineNumbers > t) && (i.updateLineNumbers = t), e.curOp.viewChanged = !0, t >= i.viewTo) Ne && Qe(e.doc, t) < i.viewTo && Wi(e);
                    else if (n <= i.viewFrom) Ne && et(e.doc, n + r) > i.viewFrom ? Wi(e) : (i.viewFrom += r, i.viewTo += r);
                    else if (t <= i.viewFrom && n >= i.viewTo) Wi(e);
                    else if (t <= i.viewFrom) {
                        var o = Hi(e, n, n + r, 1);
                        o ? (i.view = i.view.slice(o.index), i.viewFrom = o.lineN, i.viewTo += r) : Wi(e)
                    } else if (n >= i.viewTo) {
                        var l = Hi(e, t, t, -1);
                        l ? (i.view = i.view.slice(0, l.index), i.viewTo = l.lineN) : Wi(e)
                    } else {
                        var a = Hi(e, t, t, -1),
                            s = Hi(e, n, n + r, 1);
                        a && s ? (i.view = i.view.slice(0, a.index).concat(Cn(e, a.lineN, s.lineN)).concat(i.view.slice(s.index)), i.viewTo += r) : Wi(e)
                    }
                    var u = i.externalMeasured;
                    u && (n < u.lineN ? u.lineN += r : t < u.lineN + u.size && (i.externalMeasured = null))
                }

                function Ei(e, t, n) {
                    e.curOp.viewChanged = !0;
                    var r = e.display,
                        i = e.display.externalMeasured;
                    if (i && t >= i.lineN && t < i.lineN + i.size && (r.externalMeasured = null), !(t < r.viewFrom || t >= r.viewTo)) {
                        var o = r.view[Ir(e, t)];
                        if (null != o.node) {
                            var l = o.changes || (o.changes = []); - 1 == B(l, n) && l.push(n)
                        }
                    }
                }

                function Wi(e) {
                    e.display.viewFrom = e.display.viewTo = e.doc.first, e.display.view = [], e.display.viewOffset = 0
                }

                function Hi(e, t, n, r) {
                    var i, o = Ir(e, t),
                        l = e.display.view;
                    if (!Ne || n == e.doc.first + e.doc.size) return {
                        index: o,
                        lineN: n
                    };
                    for (var a = e.display.viewFrom, s = 0; s < o; s++) a += l[s].size;
                    if (a != t) {
                        if (r > 0) {
                            if (o == l.length - 1) return null;
                            i = a + l[o].size - t, o++
                        } else i = a - t;
                        t += i, n += i
                    }
                    while (Qe(e.doc, n) != n) {
                        if (o == (r < 0 ? 0 : l.length - 1)) return null;
                        n += r * l[o - (r < 0 ? 1 : 0)].size, o += r
                    }
                    return {
                        index: o,
                        lineN: n
                    }
                }

                function Fi(e, t, n) {
                    var r = e.display,
                        i = r.view;
                    0 == i.length || t >= r.viewTo || n <= r.viewFrom ? (r.view = Cn(e, t, n), r.viewFrom = t) : (r.viewFrom > t ? r.view = Cn(e, t, r.viewFrom).concat(r.view) : r.viewFrom < t && (r.view = r.view.slice(Ir(e, t))), r.viewFrom = t, r.viewTo < n ? r.view = r.view.concat(Cn(e, r.viewTo, n)) : r.viewTo > n && (r.view = r.view.slice(0, Ir(e, n)))), r.viewTo = n
                }

                function Ii(e) {
                    for (var t = e.display.view, n = 0, r = 0; r < t.length; r++) {
                        var i = t[r];
                        i.hidden || i.node && !i.changes || ++n
                    }
                    return n
                }

                function Pi(e, t) {
                    e.doc.highlightFrontier < e.display.viewTo && e.state.highlight.set(t, I(Ri, e))
                }

                function Ri(e) {
                    var t = e.doc;
                    if (!(t.highlightFrontier >= e.display.viewTo)) {
                        var n = +new Date + e.options.workTime,
                            r = Zt(e, t.highlightFrontier),
                            i = [];
                        t.iter(r.line, Math.min(t.first + t.size, e.display.viewTo + 500), (function(o) {
                            if (r.line >= e.display.viewFrom) {
                                var l = o.styles,
                                    a = o.text.length > e.options.maxHighlightLength ? Gt(t.mode, r.state) : null,
                                    s = qt(e, o, r, !0);
                                a && (r.state = a), o.styles = s.styles;
                                var u = o.styleClasses,
                                    c = s.classes;
                                c ? o.styleClasses = c : u && (o.styleClasses = null);
                                for (var f = !l || l.length != o.styles.length || u != c && (!u || !c || u.bgClass != c.bgClass || u.textClass != c.textClass), h = 0; !f && h < l.length; ++h) f = l[h] != o.styles[h];
                                f && i.push(r.line), o.stateAfter = r.save(), r.nextLine()
                            } else o.text.length <= e.options.maxHighlightLength && Qt(e, o.text, r), o.stateAfter = r.line % 5 == 0 ? r.save() : null, r.nextLine();
                            if (+new Date > n) return Pi(e, e.options.workDelay), !0
                        })), t.highlightFrontier = r.line, t.modeFrontier = Math.max(t.modeFrontier, r.line), i.length && Mi(e, (function() {
                            for (var t = 0; t < i.length; t++) Ei(e, i[t], "text")
                        }))
                    }
                }
                var zi = function(e, t, n) {
                    var r = e.display;
                    this.viewport = t, this.visible = Xr(r, e.doc, t), this.editorIsHidden = !r.wrapper.offsetWidth, this.wrapperHeight = r.wrapper.clientHeight, this.wrapperWidth = r.wrapper.clientWidth, this.oldDisplayWidth = Xn(e), this.force = n, this.dims = Dr(e), this.events = []
                };

                function Bi(e) {
                    var t = e.display;
                    !t.scrollbarsClipped && t.scroller.offsetWidth && (t.nativeBarWidth = t.scroller.offsetWidth - t.scroller.clientWidth, t.heightForcer.style.height = Yn(e) + "px", t.sizer.style.marginBottom = -t.nativeBarWidth + "px", t.sizer.style.borderRightWidth = Yn(e) + "px", t.scrollbarsClipped = !0)
                }

                function $i(e) {
                    if (e.hasFocus()) return null;
                    var t = E();
                    if (!t || !D(e.display.lineDiv, t)) return null;
                    var n = {
                        activeElt: t
                    };
                    if (window.getSelection) {
                        var r = window.getSelection();
                        r.anchorNode && r.extend && D(e.display.lineDiv, r.anchorNode) && (n.anchorNode = r.anchorNode, n.anchorOffset = r.anchorOffset, n.focusNode = r.focusNode, n.focusOffset = r.focusOffset)
                    }
                    return n
                }

                function _i(e) {
                    if (e && e.activeElt && e.activeElt != E() && (e.activeElt.focus(), e.anchorNode && D(document.body, e.anchorNode) && D(document.body, e.focusNode))) {
                        var t = window.getSelection(),
                            n = document.createRange();
                        n.setEnd(e.anchorNode, e.anchorOffset), n.collapse(!1), t.removeAllRanges(), t.addRange(n), t.extend(e.focusNode, e.focusOffset)
                    }
                }

                function ji(e, t) {
                    var n = e.display,
                        r = e.doc;
                    if (t.editorIsHidden) return Wi(e), !1;
                    if (!t.force && t.visible.from >= n.viewFrom && t.visible.to <= n.viewTo && (null == n.updateLineNumbers || n.updateLineNumbers >= n.viewTo) && n.renderedView == n.view && 0 == Ii(e)) return !1;
                    Jr(e) && (Wi(e), t.dims = Dr(e));
                    var i = r.first + r.size,
                        o = Math.max(t.visible.from - e.options.viewportMargin, r.first),
                        l = Math.min(i, t.visible.to + e.options.viewportMargin);
                    n.viewFrom < o && o - n.viewFrom < 20 && (o = Math.max(r.first, n.viewFrom)), n.viewTo > l && n.viewTo - l < 20 && (l = Math.min(i, n.viewTo)), Ne && (o = Qe(e.doc, o), l = et(e.doc, l));
                    var a = o != n.viewFrom || l != n.viewTo || n.lastWrapHeight != t.wrapperHeight || n.lastWrapWidth != t.wrapperWidth;
                    Fi(e, o, l), n.viewOffset = rt(ue(e.doc, n.viewFrom)), e.display.mover.style.top = n.viewOffset + "px";
                    var s = Ii(e);
                    if (!a && 0 == s && !t.force && n.renderedView == n.view && (null == n.updateLineNumbers || n.updateLineNumbers >= n.viewTo)) return !1;
                    var u = $i(e);
                    return s > 4 && (n.lineDiv.style.display = "none"), Ui(e, n.updateLineNumbers, t.dims), s > 4 && (n.lineDiv.style.display = ""), n.renderedView = n.view, _i(u), M(n.cursorDiv), M(n.selectionDiv), n.gutters.style.height = n.sizer.style.minHeight = 0, a && (n.lastWrapHeight = t.wrapperHeight, n.lastWrapWidth = t.wrapperWidth, Pi(e, 400)), n.updateLineNumbers = null, !0
                }

                function Gi(e, t) {
                    for (var n = t.viewport, r = !0;; r = !1) {
                        if ((!r || !e.options.lineWrapping || t.oldDisplayWidth == Xn(e)) && (n && null != n.top && (n = {
                                top: Math.min(e.doc.height + Un(e.display) - qn(e), n.top)
                            }), t.visible = Xr(e.display, e.doc, n), t.visible.from >= e.display.viewFrom && t.visible.to <= e.display.viewTo)) break;
                        if (!ji(e, t)) break;
                        Kr(e);
                        var i = fi(e);
                        Pr(e), pi(e, i), Yi(e, i), t.force = !1
                    }
                    t.signal(e, "update", e), e.display.viewFrom == e.display.reportedViewFrom && e.display.viewTo == e.display.reportedViewTo || (t.signal(e, "viewportChange", e, e.display.viewFrom, e.display.viewTo), e.display.reportedViewFrom = e.display.viewFrom, e.display.reportedViewTo = e.display.viewTo)
                }

                function Vi(e, t) {
                    var n = new zi(e, t);
                    if (ji(e, n)) {
                        Kr(e), Gi(e, n);
                        var r = fi(e);
                        Pr(e), pi(e, r), Yi(e, r), n.finish()
                    }
                }

                function Ui(e, t, n) {
                    var r = e.display,
                        i = e.options.lineNumbers,
                        o = r.lineDiv,
                        l = o.firstChild;

                    function a(t) {
                        var n = t.nextSibling;
                        return s && y && e.display.currentWheelTarget == t ? t.style.display = "none" : t.parentNode.removeChild(t), n
                    }
                    for (var u = r.view, c = r.viewFrom, f = 0; f < u.length; f++) {
                        var h = u[f];
                        if (h.hidden);
                        else if (h.node && h.node.parentNode == o) {
                            while (l != h.node) l = a(l);
                            var d = i && null != t && t <= c && h.lineNumber;
                            h.changes && (B(h.changes, "gutter") > -1 && (d = !1), Dn(e, h, c, n)), d && (M(h.lineNumber), h.lineNumber.appendChild(document.createTextNode(ve(e.options, c)))), l = h.node.nextSibling
                        } else {
                            var p = zn(e, h, c, n);
                            o.insertBefore(p, l)
                        }
                        c += h.size
                    }
                    while (l) l = a(l)
                }

                function Ki(e) {
                    var t = e.display.gutters.offsetWidth;
                    e.display.sizer.style.marginLeft = t + "px"
                }

                function Yi(e, t) {
                    e.display.sizer.style.minHeight = t.docHeight + "px", e.display.heightForcer.style.top = t.docHeight + "px", e.display.gutters.style.height = t.docHeight + e.display.barHeight + Yn(e) + "px"
                }

                function Xi(e) {
                    var t = e.display.gutters,
                        n = e.options.gutters;
                    M(t);
                    for (var r = 0; r < n.length; ++r) {
                        var i = n[r],
                            o = t.appendChild(O("div", null, "CodeMirror-gutter " + i));
                        "CodeMirror-linenumbers" == i && (e.display.lineGutter = o, o.style.width = (e.display.lineNumWidth || 1) + "px")
                    }
                    t.style.display = r ? "" : "none", Ki(e)
                }

                function qi(e) {
                    var t = B(e.gutters, "CodeMirror-linenumbers"); - 1 == t && e.lineNumbers ? e.gutters = e.gutters.concat(["CodeMirror-linenumbers"]) : t > -1 && !e.lineNumbers && (e.gutters = e.gutters.slice(0), e.gutters.splice(t, 1))
                }
                zi.prototype.signal = function(e, t) {
                    yt(e, t) && this.events.push(arguments)
                }, zi.prototype.finish = function() {
                    for (var e = this, t = 0; t < this.events.length; t++) gt.apply(null, e.events[t])
                };
                var Ji = 0,
                    Zi = null;

                function Qi(e) {
                    var t = e.wheelDeltaX,
                        n = e.wheelDeltaY;
                    return null == t && e.detail && e.axis == e.HORIZONTAL_AXIS && (t = e.detail), null == n && e.detail && e.axis == e.VERTICAL_AXIS ? n = e.detail : null == n && (n = e.wheelDelta), {
                        x: t,
                        y: n
                    }
                }

                function eo(e) {
                    var t = Qi(e);
                    return t.x *= Zi, t.y *= Zi, t
                }

                function to(e, t) {
                    var r = Qi(t),
                        i = r.x,
                        o = r.y,
                        l = e.display,
                        a = l.scroller,
                        u = a.scrollWidth > a.clientWidth,
                        c = a.scrollHeight > a.clientHeight;
                    if (i && u || o && c) {
                        if (o && y && s) e: for (var h = t.target, d = l.view; h != a; h = h.parentNode)
                            for (var p = 0; p < d.length; p++)
                                if (d[p].node == h) {
                                    e.display.currentWheelTarget = h;
                                    break e
                                } if (i && !n && !f && null != Zi) return o && c && si(e, Math.max(0, a.scrollTop + o * Zi)), ci(e, Math.max(0, a.scrollLeft + i * Zi)), (!o || o && c) && wt(t), void(l.wheelStartX = null);
                        if (o && null != Zi) {
                            var g = o * Zi,
                                v = e.doc.scrollTop,
                                m = v + l.wrapper.clientHeight;
                            g < 0 ? v = Math.max(0, v + g - 50) : m = Math.min(e.doc.height, m + g + 50), Vi(e, {
                                top: v,
                                bottom: m
                            })
                        }
                        Ji < 20 && (null == l.wheelStartX ? (l.wheelStartX = a.scrollLeft, l.wheelStartY = a.scrollTop, l.wheelDX = i, l.wheelDY = o, setTimeout((function() {
                            if (null != l.wheelStartX) {
                                var e = a.scrollLeft - l.wheelStartX,
                                    t = a.scrollTop - l.wheelStartY,
                                    n = t && l.wheelDY && t / l.wheelDY || e && l.wheelDX && e / l.wheelDX;
                                l.wheelStartX = l.wheelStartY = null, n && (Zi = (Zi * Ji + n) / (Ji + 1), ++Ji)
                            }
                        }), 200)) : (l.wheelDX += i, l.wheelDY += o))
                    }
                }
                l ? Zi = -.53 : n ? Zi = 15 : c ? Zi = -.7 : h && (Zi = -1 / 3);
                var no = function(e, t) {
                    this.ranges = e, this.primIndex = t
                };
                no.prototype.primary = function() {
                    return this.ranges[this.primIndex]
                }, no.prototype.equals = function(e) {
                    var t = this;
                    if (e == this) return !0;
                    if (e.primIndex != this.primIndex || e.ranges.length != this.ranges.length) return !1;
                    for (var n = 0; n < this.ranges.length; n++) {
                        var r = t.ranges[n],
                            i = e.ranges[n];
                        if (!be(r.anchor, i.anchor) || !be(r.head, i.head)) return !1
                    }
                    return !0
                }, no.prototype.deepCopy = function() {
                    for (var e = this, t = [], n = 0; n < this.ranges.length; n++) t[n] = new ro(we(e.ranges[n].anchor), we(e.ranges[n].head));
                    return new no(t, this.primIndex)
                }, no.prototype.somethingSelected = function() {
                    for (var e = this, t = 0; t < this.ranges.length; t++)
                        if (!e.ranges[t].empty()) return !0;
                    return !1
                }, no.prototype.contains = function(e, t) {
                    var n = this;
                    t || (t = e);
                    for (var r = 0; r < this.ranges.length; r++) {
                        var i = n.ranges[r];
                        if (ye(t, i.from()) >= 0 && ye(e, i.to()) <= 0) return r
                    }
                    return -1
                };
                var ro = function(e, t) {
                    this.anchor = e, this.head = t
                };

                function io(e, t, n) {
                    var r = e && e.options.selectionsMayTouch,
                        i = t[n];
                    t.sort((function(e, t) {
                        return ye(e.from(), t.from())
                    })), n = B(t, i);
                    for (var o = 1; o < t.length; o++) {
                        var l = t[o],
                            a = t[o - 1],
                            s = ye(a.to(), l.from());
                        if (r && !l.empty() ? s > 0 : s >= 0) {
                            var u = ke(a.from(), l.from()),
                                c = xe(a.to(), l.to()),
                                f = a.empty() ? l.from() == l.head : a.from() == a.head;
                            o <= n && --n, t.splice(--o, 2, new ro(f ? c : u, f ? u : c))
                        }
                    }
                    return new no(t, n)
                }

                function oo(e, t) {
                    return new no([new ro(e, t || e)], 0)
                }

                function lo(e) {
                    return e.text ? me(e.from.line + e.text.length - 1, X(e.text).length + (1 == e.text.length ? e.from.ch : 0)) : e.to
                }

                function ao(e, t) {
                    if (ye(e, t.from) < 0) return e;
                    if (ye(e, t.to) <= 0) return lo(t);
                    var n = e.line + t.text.length - (t.to.line - t.from.line) - 1,
                        r = e.ch;
                    return e.line == t.to.line && (r += lo(t).ch - t.to.ch), me(n, r)
                }

                function so(e, t) {
                    for (var n = [], r = 0; r < e.sel.ranges.length; r++) {
                        var i = e.sel.ranges[r];
                        n.push(new ro(ao(i.anchor, t), ao(i.head, t)))
                    }
                    return io(e.cm, n, e.sel.primIndex)
                }

                function uo(e, t, n) {
                    return e.line == t.line ? me(n.line, e.ch - t.ch + n.ch) : me(n.line + (e.line - t.line), e.ch)
                }

                function co(e, t, n) {
                    for (var r = [], i = me(e.first, 0), o = i, l = 0; l < t.length; l++) {
                        var a = t[l],
                            s = uo(a.from, i, o),
                            u = uo(lo(a), i, o);
                        if (i = a.to, o = u, "around" == n) {
                            var c = e.sel.ranges[l],
                                f = ye(c.head, c.anchor) < 0;
                            r[l] = new ro(f ? u : s, f ? s : u)
                        } else r[l] = new ro(s, s)
                    }
                    return new no(r, e.sel.primIndex)
                }

                function fo(e) {
                    e.doc.mode = $t(e.options, e.doc.modeOption), ho(e)
                }

                function ho(e) {
                    e.doc.iter((function(e) {
                        e.stateAfter && (e.stateAfter = null), e.styles && (e.styles = null)
                    })), e.doc.modeFrontier = e.doc.highlightFrontier = e.doc.first, Pi(e, 100), e.state.modeGen++, e.curOp && Di(e)
                }

                function po(e, t) {
                    return 0 == t.from.ch && 0 == t.to.ch && "" == X(t.text) && (!e.cm || e.cm.options.wholeLineUpdateBefore)
                }

                function go(e, t, n, r) {
                    function i(e) {
                        return n ? n[e] : null
                    }

                    function o(e, n, i) {
                        cn(e, n, i, r), On(e, "change", e, t)
                    }

                    function l(e, t) {
                        for (var n = [], o = e; o < t; ++o) n.push(new un(u[o], i(o), r));
                        return n
                    }
                    var a = t.from,
                        s = t.to,
                        u = t.text,
                        c = ue(e, a.line),
                        f = ue(e, s.line),
                        h = X(u),
                        d = i(u.length - 1),
                        p = s.line - a.line;
                    if (t.full) e.insert(0, l(0, u.length)), e.remove(u.length, e.size - u.length);
                    else if (po(e, t)) {
                        var g = l(0, u.length - 1);
                        o(f, f.text, d), p && e.remove(a.line, p), g.length && e.insert(a.line, g)
                    } else if (c == f)
                        if (1 == u.length) o(c, c.text.slice(0, a.ch) + h + c.text.slice(s.ch), d);
                        else {
                            var v = l(1, u.length - 1);
                            v.push(new un(h + c.text.slice(s.ch), d, r)), o(c, c.text.slice(0, a.ch) + u[0], i(0)), e.insert(a.line + 1, v)
                        }
                    else if (1 == u.length) o(c, c.text.slice(0, a.ch) + u[0] + f.text.slice(s.ch), i(0)), e.remove(a.line + 1, p);
                    else {
                        o(c, c.text.slice(0, a.ch) + u[0], i(0)), o(f, h + f.text.slice(s.ch), d);
                        var m = l(1, u.length - 1);
                        p > 1 && e.remove(a.line + 1, p - 1), e.insert(a.line + 1, m)
                    }
                    On(e, "change", e, t)
                }

                function vo(e, t, n) {
                    function r(e, i, o) {
                        if (e.linked)
                            for (var l = 0; l < e.linked.length; ++l) {
                                var a = e.linked[l];
                                if (a.doc != i) {
                                    var s = o && a.sharedHist;
                                    n && !s || (t(a.doc, s), r(a.doc, e, s))
                                }
                            }
                    }
                    r(e, null, !0)
                }

                function mo(e, t) {
                    if (t.cm) throw new Error("This document is already in use.");
                    e.doc = t, t.cm = e, Hr(e), fo(e), yo(e), e.options.lineWrapping || ot(e), e.options.mode = t.modeOption, Di(e)
                }

                function yo(e) {
                    ("rtl" == e.doc.direction ? W : T)(e.display.lineDiv, "CodeMirror-rtl")
                }

                function bo(e) {
                    Mi(e, (function() {
                        yo(e), Di(e)
                    }))
                }

                function wo(e) {
                    this.done = [], this.undone = [], this.undoDepth = 1 / 0, this.lastModTime = this.lastSelTime = 0, this.lastOp = this.lastSelOp = null, this.lastOrigin = this.lastSelOrigin = null, this.generation = this.maxGeneration = e || 1
                }

                function xo(e, t) {
                    var n = {
                        from: we(t.from),
                        to: lo(t),
                        text: ce(e, t.from, t.to)
                    };
                    return No(e, n, t.from.line, t.to.line + 1), vo(e, (function(e) {
                        return No(e, n, t.from.line, t.to.line + 1)
                    }), !0), n
                }

                function ko(e) {
                    while (e.length) {
                        var t = X(e);
                        if (!t.ranges) break;
                        e.pop()
                    }
                }

                function Co(e, t) {
                    return t ? (ko(e.done), X(e.done)) : e.done.length && !X(e.done).ranges ? X(e.done) : e.done.length > 1 && !e.done[e.done.length - 2].ranges ? (e.done.pop(), X(e.done)) : void 0
                }

                function So(e, t, n, r) {
                    var i = e.history;
                    i.undone.length = 0;
                    var o, l, a = +new Date;
                    if ((i.lastOp == r || i.lastOrigin == t.origin && t.origin && ("+" == t.origin.charAt(0) && i.lastModTime > a - (e.cm ? e.cm.options.historyEventDelay : 500) || "*" == t.origin.charAt(0))) && (o = Co(i, i.lastOp == r))) l = X(o.changes), 0 == ye(t.from, t.to) && 0 == ye(t.from, l.to) ? l.to = lo(t) : o.changes.push(xo(e, t));
                    else {
                        var s = X(i.done);
                        s && s.ranges || Mo(e.sel, i.done), o = {
                            changes: [xo(e, t)],
                            generation: i.generation
                        }, i.done.push(o);
                        while (i.done.length > i.undoDepth) i.done.shift(), i.done[0].ranges || i.done.shift()
                    }
                    i.done.push(n), i.generation = ++i.maxGeneration, i.lastModTime = i.lastSelTime = a, i.lastOp = i.lastSelOp = r, i.lastOrigin = i.lastSelOrigin = t.origin, l || gt(e, "historyAdded")
                }

                function Lo(e, t, n, r) {
                    var i = t.charAt(0);
                    return "*" == i || "+" == i && n.ranges.length == r.ranges.length && n.somethingSelected() == r.somethingSelected() && new Date - e.history.lastSelTime <= (e.cm ? e.cm.options.historyEventDelay : 500)
                }

                function To(e, t, n, r) {
                    var i = e.history,
                        o = r && r.origin;
                    n == i.lastSelOp || o && i.lastSelOrigin == o && (i.lastModTime == i.lastSelTime && i.lastOrigin == o || Lo(e, o, X(i.done), t)) ? i.done[i.done.length - 1] = t : Mo(t, i.done), i.lastSelTime = +new Date, i.lastSelOrigin = o, i.lastSelOp = n, r && !1 !== r.clearRedo && ko(i.undone)
                }

                function Mo(e, t) {
                    var n = X(t);
                    n && n.ranges && n.equals(e) || t.push(e)
                }

                function No(e, t, n, r) {
                    var i = t["spans_" + e.id],
                        o = 0;
                    e.iter(Math.max(e.first, n), Math.min(e.first + e.size, r), (function(n) {
                        n.markedSpans && ((i || (i = t["spans_" + e.id] = {}))[o] = n.markedSpans), ++o
                    }))
                }

                function Oo(e) {
                    if (!e) return null;
                    for (var t, n = 0; n < e.length; ++n) e[n].marker.explicitlyCleared ? t || (t = e.slice(0, n)) : t && t.push(e[n]);
                    return t ? t.length ? t : null : e
                }

                function Ao(e, t) {
                    var n = t["spans_" + e.id];
                    if (!n) return null;
                    for (var r = [], i = 0; i < t.text.length; ++i) r.push(Oo(n[i]));
                    return r
                }

                function Do(e, t) {
                    var n = Ao(e, t),
                        r = Pe(e, t);
                    if (!n) return r;
                    if (!r) return n;
                    for (var i = 0; i < n.length; ++i) {
                        var o = n[i],
                            l = r[i];
                        if (o && l) e: for (var a = 0; a < l.length; ++a) {
                            for (var s = l[a], u = 0; u < o.length; ++u)
                                if (o[u].marker == s.marker) continue e;
                            o.push(s)
                        } else l && (n[i] = l)
                    }
                    return n
                }

                function Eo(e, t, n) {
                    for (var r = [], i = 0; i < e.length; ++i) {
                        var o = e[i];
                        if (o.ranges) r.push(n ? no.prototype.deepCopy.call(o) : o);
                        else {
                            var l = o.changes,
                                a = [];
                            r.push({
                                changes: a
                            });
                            for (var s = 0; s < l.length; ++s) {
                                var u = l[s],
                                    c = void 0;
                                if (a.push({
                                        from: u.from,
                                        to: u.to,
                                        text: u.text
                                    }), t)
                                    for (var f in u)(c = f.match(/^spans_(\d+)$/)) && B(t, Number(c[1])) > -1 && (X(a)[f] = u[f], delete u[f])
                            }
                        }
                    }
                    return r
                }

                function Wo(e, t, n, r) {
                    if (r) {
                        var i = e.anchor;
                        if (n) {
                            var o = ye(t, i) < 0;
                            o != ye(n, i) < 0 ? (i = t, t = n) : o != ye(t, n) < 0 && (t = n)
                        }
                        return new ro(i, t)
                    }
                    return new ro(n || t, t)
                }

                function Ho(e, t, n, r, i) {
                    null == i && (i = e.cm && (e.cm.display.shift || e.extend)), Bo(e, new no([Wo(e.sel.primary(), t, n, i)], 0), r)
                }

                function Fo(e, t, n) {
                    for (var r = [], i = e.cm && (e.cm.display.shift || e.extend), o = 0; o < e.sel.ranges.length; o++) r[o] = Wo(e.sel.ranges[o], t[o], null, i);
                    var l = io(e.cm, r, e.sel.primIndex);
                    Bo(e, l, n)
                }

                function Io(e, t, n, r) {
                    var i = e.sel.ranges.slice(0);
                    i[t] = n, Bo(e, io(e.cm, i, e.sel.primIndex), r)
                }

                function Po(e, t, n, r) {
                    Bo(e, oo(t, n), r)
                }

                function Ro(e, t, n) {
                    var r = {
                        ranges: t.ranges,
                        update: function(t) {
                            var n = this;
                            this.ranges = [];
                            for (var r = 0; r < t.length; r++) n.ranges[r] = new ro(Se(e, t[r].anchor), Se(e, t[r].head))
                        },
                        origin: n && n.origin
                    };
                    return gt(e, "beforeSelectionChange", e, r), e.cm && gt(e.cm, "beforeSelectionChange", e.cm, r), r.ranges != t.ranges ? io(e.cm, r.ranges, r.ranges.length - 1) : t
                }

                function zo(e, t, n) {
                    var r = e.history.done,
                        i = X(r);
                    i && i.ranges ? (r[r.length - 1] = t, $o(e, t, n)) : Bo(e, t, n)
                }

                function Bo(e, t, n) {
                    $o(e, t, n), To(e, e.sel, e.cm ? e.cm.curOp.id : NaN, n)
                }

                function $o(e, t, n) {
                    (yt(e, "beforeSelectionChange") || e.cm && yt(e.cm, "beforeSelectionChange")) && (t = Ro(e, t, n));
                    var r = n && n.bias || (ye(t.primary().head, e.sel.primary().head) < 0 ? -1 : 1);
                    _o(e, Go(e, t, r, !0)), n && !1 === n.scroll || !e.cm || ri(e.cm)
                }

                function _o(e, t) {
                    t.equals(e.sel) || (e.sel = t, e.cm && (e.cm.curOp.updateInput = 1, e.cm.curOp.selectionChanged = !0, mt(e.cm)), On(e, "cursorActivity", e))
                }

                function jo(e) {
                    _o(e, Go(e, e.sel, null, !1))
                }

                function Go(e, t, n, r) {
                    for (var i, o = 0; o < t.ranges.length; o++) {
                        var l = t.ranges[o],
                            a = t.ranges.length == e.sel.ranges.length && e.sel.ranges[o],
                            s = Uo(e, l.anchor, a && a.anchor, n, r),
                            u = Uo(e, l.head, a && a.head, n, r);
                        (i || s != l.anchor || u != l.head) && (i || (i = t.ranges.slice(0, o)), i[o] = new ro(s, u))
                    }
                    return i ? io(e.cm, i, t.primIndex) : t
                }

                function Vo(e, t, n, r, i) {
                    var o = ue(e, t.line);
                    if (o.markedSpans)
                        for (var l = 0; l < o.markedSpans.length; ++l) {
                            var a = o.markedSpans[l],
                                s = a.marker;
                            if ((null == a.from || (s.inclusiveLeft ? a.from <= t.ch : a.from < t.ch)) && (null == a.to || (s.inclusiveRight ? a.to >= t.ch : a.to > t.ch))) {
                                if (i && (gt(s, "beforeCursorEnter"), s.explicitlyCleared)) {
                                    if (o.markedSpans) {
                                        --l;
                                        continue
                                    }
                                    break
                                }
                                if (!s.atomic) continue;
                                if (n) {
                                    var u = s.find(r < 0 ? 1 : -1),
                                        c = void 0;
                                    if ((r < 0 ? s.inclusiveRight : s.inclusiveLeft) && (u = Ko(e, u, -r, u && u.line == t.line ? o : null)), u && u.line == t.line && (c = ye(u, n)) && (r < 0 ? c < 0 : c > 0)) return Vo(e, u, t, r, i)
                                }
                                var f = s.find(r < 0 ? -1 : 1);
                                return (r < 0 ? s.inclusiveLeft : s.inclusiveRight) && (f = Ko(e, f, r, f.line == t.line ? o : null)), f ? Vo(e, f, t, r, i) : null
                            }
                        }
                    return t
                }

                function Uo(e, t, n, r, i) {
                    var o = r || 1,
                        l = Vo(e, t, n, o, i) || !i && Vo(e, t, n, o, !0) || Vo(e, t, n, -o, i) || !i && Vo(e, t, n, -o, !0);
                    return l || (e.cantEdit = !0, me(e.first, 0))
                }

                function Ko(e, t, n, r) {
                    return n < 0 && 0 == t.ch ? t.line > e.first ? Se(e, me(t.line - 1)) : null : n > 0 && t.ch == (r || ue(e, t.line)).text.length ? t.line < e.first + e.size - 1 ? me(t.line + 1, 0) : null : new me(t.line, t.ch + n)
                }

                function Yo(e) {
                    e.setSelection(me(e.firstLine(), 0), me(e.lastLine()), j)
                }

                function Xo(e, t, n) {
                    var r = {
                        canceled: !1,
                        from: t.from,
                        to: t.to,
                        text: t.text,
                        origin: t.origin,
                        cancel: function() {
                            return r.canceled = !0
                        }
                    };
                    return n && (r.update = function(t, n, i, o) {
                        t && (r.from = Se(e, t)), n && (r.to = Se(e, n)), i && (r.text = i), void 0 !== o && (r.origin = o)
                    }), gt(e, "beforeChange", e, r), e.cm && gt(e.cm, "beforeChange", e.cm, r), r.canceled ? (e.cm && (e.cm.curOp.updateInput = 2), null) : {
                        from: r.from,
                        to: r.to,
                        text: r.text,
                        origin: r.origin
                    }
                }

                function qo(e, t, n) {
                    if (e.cm) {
                        if (!e.cm.curOp) return Ni(e.cm, qo)(e, t, n);
                        if (e.cm.state.suppressEdits) return
                    }
                    if (!(yt(e, "beforeChange") || e.cm && yt(e.cm, "beforeChange")) || (t = Xo(e, t, !0), t)) {
                        var r = Me && !n && ze(e, t.from, t.to);
                        if (r)
                            for (var i = r.length - 1; i >= 0; --i) Jo(e, {
                                from: r[i].from,
                                to: r[i].to,
                                text: i ? [""] : t.text,
                                origin: t.origin
                            });
                        else Jo(e, t)
                    }
                }

                function Jo(e, t) {
                    if (1 != t.text.length || "" != t.text[0] || 0 != ye(t.from, t.to)) {
                        var n = so(e, t);
                        So(e, t, n, e.cm ? e.cm.curOp.id : NaN), el(e, t, n, Pe(e, t));
                        var r = [];
                        vo(e, (function(e, n) {
                            n || -1 != B(r, e.history) || (ol(e.history, t), r.push(e.history)), el(e, t, null, Pe(e, t))
                        }))
                    }
                }

                function Zo(e, t, n) {
                    var r = e.cm && e.cm.state.suppressEdits;
                    if (!r || n) {
                        for (var i, o = e.history, l = e.sel, a = "undo" == t ? o.done : o.undone, s = "undo" == t ? o.undone : o.done, u = 0; u < a.length; u++)
                            if (i = a[u], n ? i.ranges && !i.equals(e.sel) : !i.ranges) break;
                        if (u != a.length) {
                            for (o.lastOrigin = o.lastSelOrigin = null;;) {
                                if (i = a.pop(), !i.ranges) {
                                    if (r) return void a.push(i);
                                    break
                                }
                                if (Mo(i, s), n && !i.equals(e.sel)) return void Bo(e, i, {
                                    clearRedo: !1
                                });
                                l = i
                            }
                            var c = [];
                            Mo(l, s), s.push({
                                changes: c,
                                generation: o.generation
                            }), o.generation = i.generation || ++o.maxGeneration;
                            for (var f = yt(e, "beforeChange") || e.cm && yt(e.cm, "beforeChange"), h = function(n) {
                                    var r = i.changes[n];
                                    if (r.origin = t, f && !Xo(e, r, !1)) return a.length = 0, {};
                                    c.push(xo(e, r));
                                    var o = n ? so(e, r) : X(a);
                                    el(e, r, o, Do(e, r)), !n && e.cm && e.cm.scrollIntoView({
                                        from: r.from,
                                        to: lo(r)
                                    });
                                    var l = [];
                                    vo(e, (function(e, t) {
                                        t || -1 != B(l, e.history) || (ol(e.history, r), l.push(e.history)), el(e, r, null, Do(e, r))
                                    }))
                                }, d = i.changes.length - 1; d >= 0; --d) {
                                var p = h(d);
                                if (p) return p.v
                            }
                        }
                    }
                }

                function Qo(e, t) {
                    if (0 != t && (e.first += t, e.sel = new no(q(e.sel.ranges, (function(e) {
                            return new ro(me(e.anchor.line + t, e.anchor.ch), me(e.head.line + t, e.head.ch))
                        })), e.sel.primIndex), e.cm)) {
                        Di(e.cm, e.first, e.first - t, t);
                        for (var n = e.cm.display, r = n.viewFrom; r < n.viewTo; r++) Ei(e.cm, r, "gutter")
                    }
                }

                function el(e, t, n, r) {
                    if (e.cm && !e.cm.curOp) return Ni(e.cm, el)(e, t, n, r);
                    if (t.to.line < e.first) Qo(e, t.text.length - 1 - (t.to.line - t.from.line));
                    else if (!(t.from.line > e.lastLine())) {
                        if (t.from.line < e.first) {
                            var i = t.text.length - 1 - (e.first - t.from.line);
                            Qo(e, i), t = {
                                from: me(e.first, 0),
                                to: me(t.to.line + i, t.to.ch),
                                text: [X(t.text)],
                                origin: t.origin
                            }
                        }
                        var o = e.lastLine();
                        t.to.line > o && (t = {
                            from: t.from,
                            to: me(o, ue(e, o).text.length),
                            text: [t.text[0]],
                            origin: t.origin
                        }), t.removed = ce(e, t.from, t.to), n || (n = so(e, t)), e.cm ? tl(e.cm, t, r) : go(e, t, r), $o(e, n, j)
                    }
                }

                function tl(e, t, n) {
                    var r = e.doc,
                        i = e.display,
                        o = t.from,
                        l = t.to,
                        a = !1,
                        s = o.line;
                    e.options.lineWrapping || (s = de(qe(ue(r, o.line))), r.iter(s, l.line + 1, (function(e) {
                        if (e == i.maxLine) return a = !0, !0
                    }))), r.sel.contains(t.from, t.to) > -1 && mt(e), go(r, t, n, Wr(e)), e.options.lineWrapping || (r.iter(s, o.line + t.text.length, (function(e) {
                        var t = it(e);
                        t > i.maxLineLength && (i.maxLine = e, i.maxLineLength = t, i.maxLineChanged = !0, a = !1)
                    })), a && (e.curOp.updateMaxLine = !0)), sn(r, o.line), Pi(e, 400);
                    var u = t.text.length - (l.line - o.line) - 1;
                    t.full ? Di(e) : o.line != l.line || 1 != t.text.length || po(e.doc, t) ? Di(e, o.line, l.line + 1, u) : Ei(e, o.line, "text");
                    var c = yt(e, "changes"),
                        f = yt(e, "change");
                    if (f || c) {
                        var h = {
                            from: o,
                            to: l,
                            text: t.text,
                            removed: t.removed,
                            origin: t.origin
                        };
                        f && On(e, "change", e, h), c && (e.curOp.changeObjs || (e.curOp.changeObjs = [])).push(h)
                    }
                    e.display.selForContextMenu = null
                }

                function nl(e, t, n, r, i) {
                    var o;
                    r || (r = n), ye(r, n) < 0 && (o = [r, n], n = o[0], r = o[1]), "string" == typeof t && (t = e.splitLines(t)), qo(e, {
                        from: n,
                        to: r,
                        text: t,
                        origin: i
                    })
                }

                function rl(e, t, n, r) {
                    n < e.line ? e.line += r : t < e.line && (e.line = t, e.ch = 0)
                }

                function il(e, t, n, r) {
                    for (var i = 0; i < e.length; ++i) {
                        var o = e[i],
                            l = !0;
                        if (o.ranges) {
                            o.copied || (o = e[i] = o.deepCopy(), o.copied = !0);
                            for (var a = 0; a < o.ranges.length; a++) rl(o.ranges[a].anchor, t, n, r), rl(o.ranges[a].head, t, n, r)
                        } else {
                            for (var s = 0; s < o.changes.length; ++s) {
                                var u = o.changes[s];
                                if (n < u.from.line) u.from = me(u.from.line + r, u.from.ch), u.to = me(u.to.line + r, u.to.ch);
                                else if (t <= u.to.line) {
                                    l = !1;
                                    break
                                }
                            }
                            l || (e.splice(0, i + 1), i = 0)
                        }
                    }
                }

                function ol(e, t) {
                    var n = t.from.line,
                        r = t.to.line,
                        i = t.text.length - (r - n) - 1;
                    il(e.done, n, r, i), il(e.undone, n, r, i)
                }

                function ll(e, t, n, r) {
                    var i = t,
                        o = t;
                    return "number" == typeof t ? o = ue(e, Ce(e, t)) : i = de(t), null == i ? null : (r(o, i) && e.cm && Ei(e.cm, i, n), o)
                }

                function al(e) {
                    var t = this;
                    this.lines = e, this.parent = null;
                    for (var n = 0, r = 0; r < e.length; ++r) e[r].parent = t, n += e[r].height;
                    this.height = n
                }

                function sl(e) {
                    var t = this;
                    this.children = e;
                    for (var n = 0, r = 0, i = 0; i < e.length; ++i) {
                        var o = e[i];
                        n += o.chunkSize(), r += o.height, o.parent = t
                    }
                    this.size = n, this.height = r, this.parent = null
                }
                ro.prototype.from = function() {
                    return ke(this.anchor, this.head)
                }, ro.prototype.to = function() {
                    return xe(this.anchor, this.head)
                }, ro.prototype.empty = function() {
                    return this.head.line == this.anchor.line && this.head.ch == this.anchor.ch
                }, al.prototype = {
                    chunkSize: function() {
                        return this.lines.length
                    },
                    removeInner: function(e, t) {
                        for (var n = this, r = e, i = e + t; r < i; ++r) {
                            var o = n.lines[r];
                            n.height -= o.height, fn(o), On(o, "delete")
                        }
                        this.lines.splice(e, t)
                    },
                    collapse: function(e) {
                        e.push.apply(e, this.lines)
                    },
                    insertInner: function(e, t, n) {
                        var r = this;
                        this.height += n, this.lines = this.lines.slice(0, e).concat(t).concat(this.lines.slice(e));
                        for (var i = 0; i < t.length; ++i) t[i].parent = r
                    },
                    iterN: function(e, t, n) {
                        for (var r = this, i = e + t; e < i; ++e)
                            if (n(r.lines[e])) return !0
                    }
                }, sl.prototype = {
                    chunkSize: function() {
                        return this.size
                    },
                    removeInner: function(e, t) {
                        var n = this;
                        this.size -= t;
                        for (var r = 0; r < this.children.length; ++r) {
                            var i = n.children[r],
                                o = i.chunkSize();
                            if (e < o) {
                                var l = Math.min(t, o - e),
                                    a = i.height;
                                if (i.removeInner(e, l), n.height -= a - i.height, o == l && (n.children.splice(r--, 1), i.parent = null), 0 == (t -= l)) break;
                                e = 0
                            } else e -= o
                        }
                        if (this.size - t < 25 && (this.children.length > 1 || !(this.children[0] instanceof al))) {
                            var s = [];
                            this.collapse(s), this.children = [new al(s)], this.children[0].parent = this
                        }
                    },
                    collapse: function(e) {
                        for (var t = this, n = 0; n < this.children.length; ++n) t.children[n].collapse(e)
                    },
                    insertInner: function(e, t, n) {
                        var r = this;
                        this.size += t.length, this.height += n;
                        for (var i = 0; i < this.children.length; ++i) {
                            var o = r.children[i],
                                l = o.chunkSize();
                            if (e <= l) {
                                if (o.insertInner(e, t, n), o.lines && o.lines.length > 50) {
                                    for (var a = o.lines.length % 25 + 25, s = a; s < o.lines.length;) {
                                        var u = new al(o.lines.slice(s, s += 25));
                                        o.height -= u.height, r.children.splice(++i, 0, u), u.parent = r
                                    }
                                    o.lines = o.lines.slice(0, a), r.maybeSpill()
                                }
                                break
                            }
                            e -= l
                        }
                    },
                    maybeSpill: function() {
                        if (!(this.children.length <= 10)) {
                            var e = this;
                            do {
                                var t = e.children.splice(e.children.length - 5, 5),
                                    n = new sl(t);
                                if (e.parent) {
                                    e.size -= n.size, e.height -= n.height;
                                    var r = B(e.parent.children, e);
                                    e.parent.children.splice(r + 1, 0, n)
                                } else {
                                    var i = new sl(e.children);
                                    i.parent = e, e.children = [i, n], e = i
                                }
                                n.parent = e.parent
                            } while (e.children.length > 10);
                            e.parent.maybeSpill()
                        }
                    },
                    iterN: function(e, t, n) {
                        for (var r = this, i = 0; i < this.children.length; ++i) {
                            var o = r.children[i],
                                l = o.chunkSize();
                            if (e < l) {
                                var a = Math.min(t, l - e);
                                if (o.iterN(e, a, n)) return !0;
                                if (0 == (t -= a)) break;
                                e = 0
                            } else e -= l
                        }
                    }
                };
                var ul = function(e, t, n) {
                    var r = this;
                    if (n)
                        for (var i in n) n.hasOwnProperty(i) && (r[i] = n[i]);
                    this.doc = e, this.node = t
                };

                function cl(e, t, n) {
                    rt(t) < (e.curOp && e.curOp.scrollTop || e.doc.scrollTop) && ni(e, n)
                }

                function fl(e, t, n, r) {
                    var i = new ul(e, n, r),
                        o = e.cm;
                    return o && i.noHScroll && (o.display.alignWidgets = !0), ll(e, t, "widget", (function(t) {
                        var n = t.widgets || (t.widgets = []);
                        if (null == i.insertAt ? n.push(i) : n.splice(Math.min(n.length - 1, Math.max(0, i.insertAt)), 0, i), i.line = t, o && !tt(e, t)) {
                            var r = rt(t) < e.scrollTop;
                            he(t, t.height + jn(i)), r && ni(o, i.height), o.curOp.forceUpdate = !0
                        }
                        return !0
                    })), o && On(o, "lineWidgetAdded", o, i, "number" == typeof t ? t : de(t)), i
                }
                ul.prototype.clear = function() {
                    var e = this,
                        t = this.doc.cm,
                        n = this.line.widgets,
                        r = this.line,
                        i = de(r);
                    if (null != i && n) {
                        for (var o = 0; o < n.length; ++o) n[o] == e && n.splice(o--, 1);
                        n.length || (r.widgets = null);
                        var l = jn(this);
                        he(r, Math.max(0, r.height - l)), t && (Mi(t, (function() {
                            cl(t, r, -l), Ei(t, i, "widget")
                        })), On(t, "lineWidgetCleared", t, this, i))
                    }
                }, ul.prototype.changed = function() {
                    var e = this,
                        t = this.height,
                        n = this.doc.cm,
                        r = this.line;
                    this.height = null;
                    var i = jn(this) - t;
                    i && (tt(this.doc, r) || he(r, r.height + i), n && Mi(n, (function() {
                        n.curOp.forceUpdate = !0, cl(n, r, i), On(n, "lineWidgetChanged", n, e, de(r))
                    })))
                }, bt(ul);
                var hl = 0,
                    dl = function(e, t) {
                        this.lines = [], this.type = t, this.doc = e, this.id = ++hl
                    };

                function pl(e, t, n, r, i) {
                    if (r && r.shared) return vl(e, t, n, r, i);
                    if (e.cm && !e.cm.curOp) return Ni(e.cm, pl)(e, t, n, r, i);
                    var o = new dl(e, i),
                        l = ye(t, n);
                    if (r && P(r, o, !1), l > 0 || 0 == l && !1 !== o.clearWhenEmpty) return o;
                    if (o.replacedWith && (o.collapsed = !0, o.widgetNode = A("span", [o.replacedWith], "CodeMirror-widget"), r.handleMouseEvents || o.widgetNode.setAttribute("cm-ignore-events", "true"), r.insertLeft && (o.widgetNode.insertLeft = !0)), o.collapsed) {
                        if (Xe(e, t.line, t, n, o) || t.line != n.line && Xe(e, n.line, t, n, o)) throw new Error("Inserting collapsed marker partially overlapping an existing one");
                        Ae()
                    }
                    o.addToHistory && So(e, {
                        from: t,
                        to: n,
                        origin: "markText"
                    }, e.sel, NaN);
                    var a, s = t.line,
                        u = e.cm;
                    if (e.iter(s, n.line + 1, (function(e) {
                            u && o.collapsed && !u.options.lineWrapping && qe(e) == u.display.maxLine && (a = !0), o.collapsed && s != t.line && he(e, 0), He(e, new De(o, s == t.line ? t.ch : null, s == n.line ? n.ch : null)), ++s
                        })), o.collapsed && e.iter(t.line, n.line + 1, (function(t) {
                            tt(e, t) && he(t, 0)
                        })), o.clearOnEnter && ht(o, "beforeCursorEnter", (function() {
                            return o.clear()
                        })), o.readOnly && (Oe(), (e.history.done.length || e.history.undone.length) && e.clearHistory()), o.collapsed && (o.id = ++hl, o.atomic = !0), u) {
                        if (a && (u.curOp.updateMaxLine = !0), o.collapsed) Di(u, t.line, n.line + 1);
                        else if (o.className || o.startStyle || o.endStyle || o.css || o.attributes || o.title)
                            for (var c = t.line; c <= n.line; c++) Ei(u, c, "text");
                        o.atomic && jo(u.doc), On(u, "markerAdded", u, o)
                    }
                    return o
                }
                dl.prototype.clear = function() {
                    var e = this;
                    if (!this.explicitlyCleared) {
                        var t = this.doc.cm,
                            n = t && !t.curOp;
                        if (n && bi(t), yt(this, "clear")) {
                            var r = this.find();
                            r && On(this, "clear", r.from, r.to)
                        }
                        for (var i = null, o = null, l = 0; l < this.lines.length; ++l) {
                            var a = e.lines[l],
                                s = Ee(a.markedSpans, e);
                            t && !e.collapsed ? Ei(t, de(a), "text") : t && (null != s.to && (o = de(a)), null != s.from && (i = de(a))), a.markedSpans = We(a.markedSpans, s), null == s.from && e.collapsed && !tt(e.doc, a) && t && he(a, Or(t.display))
                        }
                        if (t && this.collapsed && !t.options.lineWrapping)
                            for (var u = 0; u < this.lines.length; ++u) {
                                var c = qe(e.lines[u]),
                                    f = it(c);
                                f > t.display.maxLineLength && (t.display.maxLine = c, t.display.maxLineLength = f, t.display.maxLineChanged = !0)
                            }
                        null != i && t && this.collapsed && Di(t, i, o + 1), this.lines.length = 0, this.explicitlyCleared = !0, this.atomic && this.doc.cantEdit && (this.doc.cantEdit = !1, t && jo(t.doc)), t && On(t, "markerCleared", t, this, i, o), n && wi(t), this.parent && this.parent.clear()
                    }
                }, dl.prototype.find = function(e, t) {
                    var n, r, i = this;
                    null == e && "bookmark" == this.type && (e = 1);
                    for (var o = 0; o < this.lines.length; ++o) {
                        var l = i.lines[o],
                            a = Ee(l.markedSpans, i);
                        if (null != a.from && (n = me(t ? l : de(l), a.from), -1 == e)) return n;
                        if (null != a.to && (r = me(t ? l : de(l), a.to), 1 == e)) return r
                    }
                    return n && {
                        from: n,
                        to: r
                    }
                }, dl.prototype.changed = function() {
                    var e = this,
                        t = this.find(-1, !0),
                        n = this,
                        r = this.doc.cm;
                    t && r && Mi(r, (function() {
                        var i = t.line,
                            o = de(t.line),
                            l = tr(r, o);
                        if (l && (cr(l), r.curOp.selectionChanged = r.curOp.forceUpdate = !0), r.curOp.updateMaxLine = !0, !tt(n.doc, i) && null != n.height) {
                            var a = n.height;
                            n.height = null;
                            var s = jn(n) - a;
                            s && he(i, i.height + s)
                        }
                        On(r, "markerChanged", r, e)
                    }))
                }, dl.prototype.attachLine = function(e) {
                    if (!this.lines.length && this.doc.cm) {
                        var t = this.doc.cm.curOp;
                        t.maybeHiddenMarkers && -1 != B(t.maybeHiddenMarkers, this) || (t.maybeUnhiddenMarkers || (t.maybeUnhiddenMarkers = [])).push(this)
                    }
                    this.lines.push(e)
                }, dl.prototype.detachLine = function(e) {
                    if (this.lines.splice(B(this.lines, e), 1), !this.lines.length && this.doc.cm) {
                        var t = this.doc.cm.curOp;
                        (t.maybeHiddenMarkers || (t.maybeHiddenMarkers = [])).push(this)
                    }
                }, bt(dl);
                var gl = function(e, t) {
                    var n = this;
                    this.markers = e, this.primary = t;
                    for (var r = 0; r < e.length; ++r) e[r].parent = n
                };

                function vl(e, t, n, r, i) {
                    r = P(r), r.shared = !1;
                    var o = [pl(e, t, n, r, i)],
                        l = o[0],
                        a = r.widgetNode;
                    return vo(e, (function(e) {
                        a && (r.widgetNode = a.cloneNode(!0)), o.push(pl(e, Se(e, t), Se(e, n), r, i));
                        for (var s = 0; s < e.linked.length; ++s)
                            if (e.linked[s].isParent) return;
                        l = X(o)
                    })), new gl(o, l)
                }

                function ml(e) {
                    return e.findMarks(me(e.first, 0), e.clipPos(me(e.lastLine())), (function(e) {
                        return e.parent
                    }))
                }

                function yl(e, t) {
                    for (var n = 0; n < t.length; n++) {
                        var r = t[n],
                            i = r.find(),
                            o = e.clipPos(i.from),
                            l = e.clipPos(i.to);
                        if (ye(o, l)) {
                            var a = pl(e, o, l, r.primary, r.primary.type);
                            r.markers.push(a), a.parent = r
                        }
                    }
                }

                function bl(e) {
                    for (var t = function(t) {
                            var n = e[t],
                                r = [n.primary.doc];
                            vo(n.primary.doc, (function(e) {
                                return r.push(e)
                            }));
                            for (var i = 0; i < n.markers.length; i++) {
                                var o = n.markers[i]; - 1 == B(r, o.doc) && (o.parent = null, n.markers.splice(i--, 1))
                            }
                        }, n = 0; n < e.length; n++) t(n)
                }
                gl.prototype.clear = function() {
                    var e = this;
                    if (!this.explicitlyCleared) {
                        this.explicitlyCleared = !0;
                        for (var t = 0; t < this.markers.length; ++t) e.markers[t].clear();
                        On(this, "clear")
                    }
                }, gl.prototype.find = function(e, t) {
                    return this.primary.find(e, t)
                }, bt(gl);
                var wl = 0,
                    xl = function(e, t, n, r, i) {
                        if (!(this instanceof xl)) return new xl(e, t, n, r, i);
                        null == n && (n = 0), sl.call(this, [new al([new un("", null)])]), this.first = n, this.scrollTop = this.scrollLeft = 0, this.cantEdit = !1, this.cleanGeneration = 1, this.modeFrontier = this.highlightFrontier = n;
                        var o = me(n, 0);
                        this.sel = oo(o), this.history = new wo(null), this.id = ++wl, this.modeOption = t, this.lineSep = r, this.direction = "rtl" == i ? "rtl" : "ltr", this.extend = !1, "string" == typeof e && (e = this.splitLines(e)), go(this, {
                            from: o,
                            to: o,
                            text: e
                        }), Bo(this, oo(o), j)
                    };
                xl.prototype = Q(sl.prototype, {
                    constructor: xl,
                    iter: function(e, t, n) {
                        n ? this.iterN(e - this.first, t - e, n) : this.iterN(this.first, this.first + this.size, e)
                    },
                    insert: function(e, t) {
                        for (var n = 0, r = 0; r < t.length; ++r) n += t[r].height;
                        this.insertInner(e - this.first, t, n)
                    },
                    remove: function(e, t) {
                        this.removeInner(e - this.first, t)
                    },
                    getValue: function(e) {
                        var t = fe(this, this.first, this.first + this.size);
                        return !1 === e ? t : t.join(e || this.lineSeparator())
                    },
                    setValue: Ai((function(e) {
                        var t = me(this.first, 0),
                            n = this.first + this.size - 1;
                        qo(this, {
                            from: t,
                            to: me(n, ue(this, n).text.length),
                            text: this.splitLines(e),
                            origin: "setValue",
                            full: !0
                        }, !0), this.cm && ii(this.cm, 0, 0), Bo(this, oo(t), j)
                    })),
                    replaceRange: function(e, t, n, r) {
                        t = Se(this, t), n = n ? Se(this, n) : t, nl(this, e, t, n, r)
                    },
                    getRange: function(e, t, n) {
                        var r = ce(this, Se(this, e), Se(this, t));
                        return !1 === n ? r : r.join(n || this.lineSeparator())
                    },
                    getLine: function(e) {
                        var t = this.getLineHandle(e);
                        return t && t.text
                    },
                    getLineHandle: function(e) {
                        if (ge(this, e)) return ue(this, e)
                    },
                    getLineNumber: function(e) {
                        return de(e)
                    },
                    getLineHandleVisualStart: function(e) {
                        return "number" == typeof e && (e = ue(this, e)), qe(e)
                    },
                    lineCount: function() {
                        return this.size
                    },
                    firstLine: function() {
                        return this.first
                    },
                    lastLine: function() {
                        return this.first + this.size - 1
                    },
                    clipPos: function(e) {
                        return Se(this, e)
                    },
                    getCursor: function(e) {
                        var t, n = this.sel.primary();
                        return t = null == e || "head" == e ? n.head : "anchor" == e ? n.anchor : "end" == e || "to" == e || !1 === e ? n.to() : n.from(), t
                    },
                    listSelections: function() {
                        return this.sel.ranges
                    },
                    somethingSelected: function() {
                        return this.sel.somethingSelected()
                    },
                    setCursor: Ai((function(e, t, n) {
                        Po(this, Se(this, "number" == typeof e ? me(e, t || 0) : e), null, n)
                    })),
                    setSelection: Ai((function(e, t, n) {
                        Po(this, Se(this, e), Se(this, t || e), n)
                    })),
                    extendSelection: Ai((function(e, t, n) {
                        Ho(this, Se(this, e), t && Se(this, t), n)
                    })),
                    extendSelections: Ai((function(e, t) {
                        Fo(this, Te(this, e), t)
                    })),
                    extendSelectionsBy: Ai((function(e, t) {
                        var n = q(this.sel.ranges, e);
                        Fo(this, Te(this, n), t)
                    })),
                    setSelections: Ai((function(e, t, n) {
                        var r = this;
                        if (e.length) {
                            for (var i = [], o = 0; o < e.length; o++) i[o] = new ro(Se(r, e[o].anchor), Se(r, e[o].head));
                            null == t && (t = Math.min(e.length - 1, this.sel.primIndex)), Bo(this, io(this.cm, i, t), n)
                        }
                    })),
                    addSelection: Ai((function(e, t, n) {
                        var r = this.sel.ranges.slice(0);
                        r.push(new ro(Se(this, e), Se(this, t || e))), Bo(this, io(this.cm, r, r.length - 1), n)
                    })),
                    getSelection: function(e) {
                        for (var t, n = this, r = this.sel.ranges, i = 0; i < r.length; i++) {
                            var o = ce(n, r[i].from(), r[i].to());
                            t = t ? t.concat(o) : o
                        }
                        return !1 === e ? t : t.join(e || this.lineSeparator())
                    },
                    getSelections: function(e) {
                        for (var t = this, n = [], r = this.sel.ranges, i = 0; i < r.length; i++) {
                            var o = ce(t, r[i].from(), r[i].to());
                            !1 !== e && (o = o.join(e || t.lineSeparator())), n[i] = o
                        }
                        return n
                    },
                    replaceSelection: function(e, t, n) {
                        for (var r = [], i = 0; i < this.sel.ranges.length; i++) r[i] = e;
                        this.replaceSelections(r, t, n || "+input")
                    },
                    replaceSelections: Ai((function(e, t, n) {
                        for (var r = this, i = [], o = this.sel, l = 0; l < o.ranges.length; l++) {
                            var a = o.ranges[l];
                            i[l] = {
                                from: a.from(),
                                to: a.to(),
                                text: r.splitLines(e[l]),
                                origin: n
                            }
                        }
                        for (var s = t && "end" != t && co(this, i, t), u = i.length - 1; u >= 0; u--) qo(r, i[u]);
                        s ? zo(this, s) : this.cm && ri(this.cm)
                    })),
                    undo: Ai((function() {
                        Zo(this, "undo")
                    })),
                    redo: Ai((function() {
                        Zo(this, "redo")
                    })),
                    undoSelection: Ai((function() {
                        Zo(this, "undo", !0)
                    })),
                    redoSelection: Ai((function() {
                        Zo(this, "redo", !0)
                    })),
                    setExtending: function(e) {
                        this.extend = e
                    },
                    getExtending: function() {
                        return this.extend
                    },
                    historySize: function() {
                        for (var e = this.history, t = 0, n = 0, r = 0; r < e.done.length; r++) e.done[r].ranges || ++t;
                        for (var i = 0; i < e.undone.length; i++) e.undone[i].ranges || ++n;
                        return {
                            undo: t,
                            redo: n
                        }
                    },
                    clearHistory: function() {
                        this.history = new wo(this.history.maxGeneration)
                    },
                    markClean: function() {
                        this.cleanGeneration = this.changeGeneration(!0)
                    },
                    changeGeneration: function(e) {
                        return e && (this.history.lastOp = this.history.lastSelOp = this.history.lastOrigin = null), this.history.generation
                    },
                    isClean: function(e) {
                        return this.history.generation == (e || this.cleanGeneration)
                    },
                    getHistory: function() {
                        return {
                            done: Eo(this.history.done),
                            undone: Eo(this.history.undone)
                        }
                    },
                    setHistory: function(e) {
                        var t = this.history = new wo(this.history.maxGeneration);
                        t.done = Eo(e.done.slice(0), null, !0), t.undone = Eo(e.undone.slice(0), null, !0)
                    },
                    setGutterMarker: Ai((function(e, t, n) {
                        return ll(this, e, "gutter", (function(e) {
                            var r = e.gutterMarkers || (e.gutterMarkers = {});
                            return r[t] = n, !n && re(r) && (e.gutterMarkers = null), !0
                        }))
                    })),
                    clearGutter: Ai((function(e) {
                        var t = this;
                        this.iter((function(n) {
                            n.gutterMarkers && n.gutterMarkers[e] && ll(t, n, "gutter", (function() {
                                return n.gutterMarkers[e] = null, re(n.gutterMarkers) && (n.gutterMarkers = null), !0
                            }))
                        }))
                    })),
                    lineInfo: function(e) {
                        var t;
                        if ("number" == typeof e) {
                            if (!ge(this, e)) return null;
                            if (t = e, e = ue(this, e), !e) return null
                        } else if (t = de(e), null == t) return null;
                        return {
                            line: t,
                            handle: e,
                            text: e.text,
                            gutterMarkers: e.gutterMarkers,
                            textClass: e.textClass,
                            bgClass: e.bgClass,
                            wrapClass: e.wrapClass,
                            widgets: e.widgets
                        }
                    },
                    addLineClass: Ai((function(e, t, n) {
                        return ll(this, e, "gutter" == t ? "gutter" : "class", (function(e) {
                            var r = "text" == t ? "textClass" : "background" == t ? "bgClass" : "gutter" == t ? "gutterClass" : "wrapClass";
                            if (e[r]) {
                                if (S(n).test(e[r])) return !1;
                                e[r] += " " + n
                            } else e[r] = n;
                            return !0
                        }))
                    })),
                    removeLineClass: Ai((function(e, t, n) {
                        return ll(this, e, "gutter" == t ? "gutter" : "class", (function(e) {
                            var r = "text" == t ? "textClass" : "background" == t ? "bgClass" : "gutter" == t ? "gutterClass" : "wrapClass",
                                i = e[r];
                            if (!i) return !1;
                            if (null == n) e[r] = null;
                            else {
                                var o = i.match(S(n));
                                if (!o) return !1;
                                var l = o.index + o[0].length;
                                e[r] = i.slice(0, o.index) + (o.index && l != i.length ? " " : "") + i.slice(l) || null
                            }
                            return !0
                        }))
                    })),
                    addLineWidget: Ai((function(e, t, n) {
                        return fl(this, e, t, n)
                    })),
                    removeLineWidget: function(e) {
                        e.clear()
                    },
                    markText: function(e, t, n) {
                        return pl(this, Se(this, e), Se(this, t), n, n && n.type || "range")
                    },
                    setBookmark: function(e, t) {
                        var n = {
                            replacedWith: t && (null == t.nodeType ? t.widget : t),
                            insertLeft: t && t.insertLeft,
                            clearWhenEmpty: !1,
                            shared: t && t.shared,
                            handleMouseEvents: t && t.handleMouseEvents
                        };
                        return e = Se(this, e), pl(this, e, e, n, "bookmark")
                    },
                    findMarksAt: function(e) {
                        e = Se(this, e);
                        var t = [],
                            n = ue(this, e.line).markedSpans;
                        if (n)
                            for (var r = 0; r < n.length; ++r) {
                                var i = n[r];
                                (null == i.from || i.from <= e.ch) && (null == i.to || i.to >= e.ch) && t.push(i.marker.parent || i.marker)
                            }
                        return t
                    },
                    findMarks: function(e, t, n) {
                        e = Se(this, e), t = Se(this, t);
                        var r = [],
                            i = e.line;
                        return this.iter(e.line, t.line + 1, (function(o) {
                            var l = o.markedSpans;
                            if (l)
                                for (var a = 0; a < l.length; a++) {
                                    var s = l[a];
                                    null != s.to && i == e.line && e.ch >= s.to || null == s.from && i != e.line || null != s.from && i == t.line && s.from >= t.ch || n && !n(s.marker) || r.push(s.marker.parent || s.marker)
                                }++i
                        })), r
                    },
                    getAllMarks: function() {
                        var e = [];
                        return this.iter((function(t) {
                            var n = t.markedSpans;
                            if (n)
                                for (var r = 0; r < n.length; ++r) null != n[r].from && e.push(n[r].marker)
                        })), e
                    },
                    posFromIndex: function(e) {
                        var t, n = this.first,
                            r = this.lineSeparator().length;
                        return this.iter((function(i) {
                            var o = i.text.length + r;
                            if (o > e) return t = e, !0;
                            e -= o, ++n
                        })), Se(this, me(n, t))
                    },
                    indexFromPos: function(e) {
                        e = Se(this, e);
                        var t = e.ch;
                        if (e.line < this.first || e.ch < 0) return 0;
                        var n = this.lineSeparator().length;
                        return this.iter(this.first, e.line, (function(e) {
                            t += e.text.length + n
                        })), t
                    },
                    copy: function(e) {
                        var t = new xl(fe(this, this.first, this.first + this.size), this.modeOption, this.first, this.lineSep, this.direction);
                        return t.scrollTop = this.scrollTop, t.scrollLeft = this.scrollLeft, t.sel = this.sel, t.extend = !1, e && (t.history.undoDepth = this.history.undoDepth, t.setHistory(this.getHistory())), t
                    },
                    linkedDoc: function(e) {
                        e || (e = {});
                        var t = this.first,
                            n = this.first + this.size;
                        null != e.from && e.from > t && (t = e.from), null != e.to && e.to < n && (n = e.to);
                        var r = new xl(fe(this, t, n), e.mode || this.modeOption, t, this.lineSep, this.direction);
                        return e.sharedHist && (r.history = this.history), (this.linked || (this.linked = [])).push({
                            doc: r,
                            sharedHist: e.sharedHist
                        }), r.linked = [{
                            doc: this,
                            isParent: !0,
                            sharedHist: e.sharedHist
                        }], yl(r, ml(this)), r
                    },
                    unlinkDoc: function(e) {
                        var t = this;
                        if (e instanceof Ia && (e = e.doc), this.linked)
                            for (var n = 0; n < this.linked.length; ++n) {
                                var r = t.linked[n];
                                if (r.doc == e) {
                                    t.linked.splice(n, 1), e.unlinkDoc(t), bl(ml(t));
                                    break
                                }
                            }
                        if (e.history == this.history) {
                            var i = [e.id];
                            vo(e, (function(e) {
                                return i.push(e.id)
                            }), !0), e.history = new wo(null), e.history.done = Eo(this.history.done, i), e.history.undone = Eo(this.history.undone, i)
                        }
                    },
                    iterLinkedDocs: function(e) {
                        vo(this, e)
                    },
                    getMode: function() {
                        return this.mode
                    },
                    getEditor: function() {
                        return this.cm
                    },
                    splitLines: function(e) {
                        return this.lineSep ? e.split(this.lineSep) : Dt(e)
                    },
                    lineSeparator: function() {
                        return this.lineSep || "\n"
                    },
                    setDirection: Ai((function(e) {
                        "rtl" != e && (e = "ltr"), e != this.direction && (this.direction = e, this.iter((function(e) {
                            return e.order = null
                        })), this.cm && bo(this.cm))
                    }))
                }), xl.prototype.eachLine = xl.prototype.iter;
                var kl = 0;

                function Cl(e) {
                    var t = this;
                    if (Tl(t), !vt(t, e) && !Gn(t.display, e)) {
                        wt(e), l && (kl = +new Date);
                        var n = Fr(t, e, !0),
                            r = e.dataTransfer.files;
                        if (n && !t.isReadOnly())
                            if (r && r.length && window.FileReader && window.File)
                                for (var i = r.length, o = Array(i), a = 0, s = function(e, r) {
                                        if (!t.options.allowDropFileTypes || -1 != B(t.options.allowDropFileTypes, e.type)) {
                                            var l = new FileReader;
                                            l.onload = Ni(t, (function() {
                                                var e = l.result;
                                                if (/[\x00-\x08\x0e-\x1f]{2}/.test(e) && (e = ""), o[r] = e, ++a == i) {
                                                    n = Se(t.doc, n);
                                                    var s = {
                                                        from: n,
                                                        to: n,
                                                        text: t.doc.splitLines(o.join(t.doc.lineSeparator())),
                                                        origin: "paste"
                                                    };
                                                    qo(t.doc, s), zo(t.doc, oo(n, lo(s)))
                                                }
                                            })), l.readAsText(e)
                                        }
                                    }, u = 0; u < i; ++u) s(r[u], u);
                            else {
                                if (t.state.draggingText && t.doc.sel.contains(n) > -1) return t.state.draggingText(e), void setTimeout((function() {
                                    return t.display.input.focus()
                                }), 20);
                                try {
                                    var c = e.dataTransfer.getData("Text");
                                    if (c) {
                                        var f;
                                        if (t.state.draggingText && !t.state.draggingText.copy && (f = t.listSelections()), $o(t.doc, oo(n, n)), f)
                                            for (var h = 0; h < f.length; ++h) nl(t.doc, "", f[h].anchor, f[h].head, "drag");
                                        t.replaceSelection(c, "around", "paste"), t.display.input.focus()
                                    }
                                } catch (e) {}
                            }
                    }
                }

                function Sl(e, t) {
                    if (l && (!e.state.draggingText || +new Date - kl < 100)) Ct(t);
                    else if (!vt(e, t) && !Gn(e.display, t) && (t.dataTransfer.setData("Text", e.getSelection()), t.dataTransfer.effectAllowed = "copyMove", t.dataTransfer.setDragImage && !h)) {
                        var n = O("img", null, null, "position: fixed; left: 0; top: 0;");
                        n.src = "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==", f && (n.width = n.height = 1, e.display.wrapper.appendChild(n), n._top = n.offsetTop), t.dataTransfer.setDragImage(n, 0, 0), f && n.parentNode.removeChild(n)
                    }
                }

                function Ll(e, t) {
                    var n = Fr(e, t);
                    if (n) {
                        var r = document.createDocumentFragment();
                        zr(e, n, r), e.display.dragCursor || (e.display.dragCursor = O("div", null, "CodeMirror-cursors CodeMirror-dragcursors"), e.display.lineSpace.insertBefore(e.display.dragCursor, e.display.cursorDiv)), N(e.display.dragCursor, r)
                    }
                }

                function Tl(e) {
                    e.display.dragCursor && (e.display.lineSpace.removeChild(e.display.dragCursor), e.display.dragCursor = null)
                }

                function Ml(e) {
                    if (document.getElementsByClassName) {
                        for (var t = document.getElementsByClassName("CodeMirror"), n = [], r = 0; r < t.length; r++) {
                            var i = t[r].CodeMirror;
                            i && n.push(i)
                        }
                        n.length && n[0].operation((function() {
                            for (var t = 0; t < n.length; t++) e(n[t])
                        }))
                    }
                }
                var Nl = !1;

                function Ol() {
                    Nl || (Al(), Nl = !0)
                }

                function Al() {
                    var e;
                    ht(window, "resize", (function() {
                        null == e && (e = setTimeout((function() {
                            e = null, Ml(Dl)
                        }), 100))
                    })), ht(window, "blur", (function() {
                        return Ml(Ur)
                    }))
                }

                function Dl(e) {
                    var t = e.display;
                    t.cachedCharWidth = t.cachedTextHeight = t.cachedPaddingH = null, t.scrollbarsClipped = !1, e.setSize()
                }
                for (var El = {
                        3: "Pause",
                        8: "Backspace",
                        9: "Tab",
                        13: "Enter",
                        16: "Shift",
                        17: "Ctrl",
                        18: "Alt",
                        19: "Pause",
                        20: "CapsLock",
                        27: "Esc",
                        32: "Space",
                        33: "PageUp",
                        34: "PageDown",
                        35: "End",
                        36: "Home",
                        37: "Left",
                        38: "Up",
                        39: "Right",
                        40: "Down",
                        44: "PrintScrn",
                        45: "Insert",
                        46: "Delete",
                        59: ";",
                        61: "=",
                        91: "Mod",
                        92: "Mod",
                        93: "Mod",
                        106: "*",
                        107: "=",
                        109: "-",
                        110: ".",
                        111: "/",
                        127: "Delete",
                        145: "ScrollLock",
                        173: "-",
                        186: ";",
                        187: "=",
                        188: ",",
                        189: "-",
                        190: ".",
                        191: "/",
                        192: "`",
                        219: "[",
                        220: "\\",
                        221: "]",
                        222: "'",
                        63232: "Up",
                        63233: "Down",
                        63234: "Left",
                        63235: "Right",
                        63272: "Delete",
                        63273: "Home",
                        63275: "End",
                        63276: "PageUp",
                        63277: "PageDown",
                        63302: "Insert"
                    }, Wl = 0; Wl < 10; Wl++) El[Wl + 48] = El[Wl + 96] = String(Wl);
                for (var Hl = 65; Hl <= 90; Hl++) El[Hl] = String.fromCharCode(Hl);
                for (var Fl = 1; Fl <= 12; Fl++) El[Fl + 111] = El[Fl + 63235] = "F" + Fl;
                var Il = {};

                function Pl(e) {
                    var t, n, r, i, o = e.split(/-(?!$)/);
                    e = o[o.length - 1];
                    for (var l = 0; l < o.length - 1; l++) {
                        var a = o[l];
                        if (/^(cmd|meta|m)$/i.test(a)) i = !0;
                        else if (/^a(lt)?$/i.test(a)) t = !0;
                        else if (/^(c|ctrl|control)$/i.test(a)) n = !0;
                        else {
                            if (!/^s(hift)?$/i.test(a)) throw new Error("Unrecognized modifier name: " + a);
                            r = !0
                        }
                    }
                    return t && (e = "Alt-" + e), n && (e = "Ctrl-" + e), i && (e = "Cmd-" + e), r && (e = "Shift-" + e), e
                }

                function Rl(e) {
                    var t = {};
                    for (var n in e)
                        if (e.hasOwnProperty(n)) {
                            var r = e[n];
                            if (/^(name|fallthrough|(de|at)tach)$/.test(n)) continue;
                            if ("..." == r) {
                                delete e[n];
                                continue
                            }
                            for (var i = q(n.split(" "), Pl), o = 0; o < i.length; o++) {
                                var l = void 0,
                                    a = void 0;
                                o == i.length - 1 ? (a = i.join(" "), l = r) : (a = i.slice(0, o + 1).join(" "), l = "...");
                                var s = t[a];
                                if (s) {
                                    if (s != l) throw new Error("Inconsistent bindings for " + a)
                                } else t[a] = l
                            }
                            delete e[n]
                        } for (var u in t) e[u] = t[u];
                    return e
                }

                function zl(e, t, n, r) {
                    t = jl(t);
                    var i = t.call ? t.call(e, r) : t[e];
                    if (!1 === i) return "nothing";
                    if ("..." === i) return "multi";
                    if (null != i && n(i)) return "handled";
                    if (t.fallthrough) {
                        if ("[object Array]" != Object.prototype.toString.call(t.fallthrough)) return zl(e, t.fallthrough, n, r);
                        for (var o = 0; o < t.fallthrough.length; o++) {
                            var l = zl(e, t.fallthrough[o], n, r);
                            if (l) return l
                        }
                    }
                }

                function Bl(e) {
                    var t = "string" == typeof e ? e : El[e.keyCode];
                    return "Ctrl" == t || "Alt" == t || "Shift" == t || "Mod" == t
                }

                function $l(e, t, n) {
                    var r = e;
                    return t.altKey && "Alt" != r && (e = "Alt-" + e), (k ? t.metaKey : t.ctrlKey) && "Ctrl" != r && (e = "Ctrl-" + e), (k ? t.ctrlKey : t.metaKey) && "Cmd" != r && (e = "Cmd-" + e), !n && t.shiftKey && "Shift" != r && (e = "Shift-" + e), e
                }

                function _l(e, t) {
                    if (f && 34 == e.keyCode && e["char"]) return !1;
                    var n = El[e.keyCode];
                    return null != n && !e.altGraphKey && (3 == e.keyCode && e.code && (n = e.code), $l(n, e, t))
                }

                function jl(e) {
                    return "string" == typeof e ? Il[e] : e
                }

                function Gl(e, t) {
                    for (var n = e.doc.sel.ranges, r = [], i = 0; i < n.length; i++) {
                        var o = t(n[i]);
                        while (r.length && ye(o.from, X(r).to) <= 0) {
                            var l = r.pop();
                            if (ye(l.from, o.from) < 0) {
                                o.from = l.from;
                                break
                            }
                        }
                        r.push(o)
                    }
                    Mi(e, (function() {
                        for (var t = r.length - 1; t >= 0; t--) nl(e.doc, "", r[t].from, r[t].to, "+delete");
                        ri(e)
                    }))
                }

                function Vl(e, t, n) {
                    var r = le(e.text, t + n, n);
                    return r < 0 || r > e.text.length ? null : r
                }

                function Ul(e, t, n) {
                    var r = Vl(e, t.ch, n);
                    return null == r ? null : new me(t.line, r, n < 0 ? "after" : "before")
                }

                function Kl(e, t, n, r, i) {
                    if (e) {
                        var o = ct(n, t.doc.direction);
                        if (o) {
                            var l, a = i < 0 ? X(o) : o[0],
                                s = i < 0 == (1 == a.level),
                                u = s ? "after" : "before";
                            if (a.level > 0 || "rtl" == t.doc.direction) {
                                var c = nr(t, n);
                                l = i < 0 ? n.text.length - 1 : 0;
                                var f = rr(t, c, l).top;
                                l = ae((function(e) {
                                    return rr(t, c, e).top == f
                                }), i < 0 == (1 == a.level) ? a.from : a.to - 1, l), "before" == u && (l = Vl(n, l, 1))
                            } else l = i < 0 ? a.to : a.from;
                            return new me(r, l, u)
                        }
                    }
                    return new me(r, i < 0 ? n.text.length : 0, i < 0 ? "before" : "after")
                }

                function Yl(e, t, n, r) {
                    var i = ct(t, e.doc.direction);
                    if (!i) return Ul(t, n, r);
                    n.ch >= t.text.length ? (n.ch = t.text.length, n.sticky = "before") : n.ch <= 0 && (n.ch = 0, n.sticky = "after");
                    var o = st(i, n.ch, n.sticky),
                        l = i[o];
                    if ("ltr" == e.doc.direction && l.level % 2 == 0 && (r > 0 ? l.to > n.ch : l.from < n.ch)) return Ul(t, n, r);
                    var a, s = function(e, n) {
                            return Vl(t, e instanceof me ? e.ch : e, n)
                        },
                        u = function(n) {
                            return e.options.lineWrapping ? (a = a || nr(e, t), Sr(e, t, a, n)) : {
                                begin: 0,
                                end: t.text.length
                            }
                        },
                        c = u("before" == n.sticky ? s(n, -1) : n.ch);
                    if ("rtl" == e.doc.direction || 1 == l.level) {
                        var f = 1 == l.level == r < 0,
                            h = s(n, f ? 1 : -1);
                        if (null != h && (f ? h <= l.to && h <= c.end : h >= l.from && h >= c.begin)) {
                            var d = f ? "before" : "after";
                            return new me(n.line, h, d)
                        }
                    }
                    var p = function(e, t, r) {
                            for (var o = function(e, t) {
                                    return t ? new me(n.line, s(e, 1), "before") : new me(n.line, e, "after")
                                }; e >= 0 && e < i.length; e += t) {
                                var l = i[e],
                                    a = t > 0 == (1 != l.level),
                                    u = a ? r.begin : s(r.end, -1);
                                if (l.from <= u && u < l.to) return o(u, a);
                                if (u = a ? l.from : s(l.to, -1), r.begin <= u && u < r.end) return o(u, a)
                            }
                        },
                        g = p(o + r, r, c);
                    if (g) return g;
                    var v = r > 0 ? c.end : s(c.begin, -1);
                    return null == v || r > 0 && v == t.text.length || (g = p(r > 0 ? 0 : i.length - 1, r, u(v)), !g) ? null : g
                }
                Il.basic = {
                    Left: "goCharLeft",
                    Right: "goCharRight",
                    Up: "goLineUp",
                    Down: "goLineDown",
                    End: "goLineEnd",
                    Home: "goLineStartSmart",
                    PageUp: "goPageUp",
                    PageDown: "goPageDown",
                    Delete: "delCharAfter",
                    Backspace: "delCharBefore",
                    "Shift-Backspace": "delCharBefore",
                    Tab: "defaultTab",
                    "Shift-Tab": "indentAuto",
                    Enter: "newlineAndIndent",
                    Insert: "toggleOverwrite",
                    Esc: "singleSelection"
                }, Il.pcDefault = {
                    "Ctrl-A": "selectAll",
                    "Ctrl-D": "deleteLine",
                    "Ctrl-Z": "undo",
                    "Shift-Ctrl-Z": "redo",
                    "Ctrl-Y": "redo",
                    "Ctrl-Home": "goDocStart",
                    "Ctrl-End": "goDocEnd",
                    "Ctrl-Up": "goLineUp",
                    "Ctrl-Down": "goLineDown",
                    "Ctrl-Left": "goGroupLeft",
                    "Ctrl-Right": "goGroupRight",
                    "Alt-Left": "goLineStart",
                    "Alt-Right": "goLineEnd",
                    "Ctrl-Backspace": "delGroupBefore",
                    "Ctrl-Delete": "delGroupAfter",
                    "Ctrl-S": "save",
                    "Ctrl-F": "find",
                    "Ctrl-G": "findNext",
                    "Shift-Ctrl-G": "findPrev",
                    "Shift-Ctrl-F": "replace",
                    "Shift-Ctrl-R": "replaceAll",
                    "Ctrl-[": "indentLess",
                    "Ctrl-]": "indentMore",
                    "Ctrl-U": "undoSelection",
                    "Shift-Ctrl-U": "redoSelection",
                    "Alt-U": "redoSelection",
                    fallthrough: "basic"
                }, Il.emacsy = {
                    "Ctrl-F": "goCharRight",
                    "Ctrl-B": "goCharLeft",
                    "Ctrl-P": "goLineUp",
                    "Ctrl-N": "goLineDown",
                    "Alt-F": "goWordRight",
                    "Alt-B": "goWordLeft",
                    "Ctrl-A": "goLineStart",
                    "Ctrl-E": "goLineEnd",
                    "Ctrl-V": "goPageDown",
                    "Shift-Ctrl-V": "goPageUp",
                    "Ctrl-D": "delCharAfter",
                    "Ctrl-H": "delCharBefore",
                    "Alt-D": "delWordAfter",
                    "Alt-Backspace": "delWordBefore",
                    "Ctrl-K": "killLine",
                    "Ctrl-T": "transposeChars",
                    "Ctrl-O": "openLine"
                }, Il.macDefault = {
                    "Cmd-A": "selectAll",
                    "Cmd-D": "deleteLine",
                    "Cmd-Z": "undo",
                    "Shift-Cmd-Z": "redo",
                    "Cmd-Y": "redo",
                    "Cmd-Home": "goDocStart",
                    "Cmd-Up": "goDocStart",
                    "Cmd-End": "goDocEnd",
                    "Cmd-Down": "goDocEnd",
                    "Alt-Left": "goGroupLeft",
                    "Alt-Right": "goGroupRight",
                    "Cmd-Left": "goLineLeft",
                    "Cmd-Right": "goLineRight",
                    "Alt-Backspace": "delGroupBefore",
                    "Ctrl-Alt-Backspace": "delGroupAfter",
                    "Alt-Delete": "delGroupAfter",
                    "Cmd-S": "save",
                    "Cmd-F": "find",
                    "Cmd-G": "findNext",
                    "Shift-Cmd-G": "findPrev",
                    "Cmd-Alt-F": "replace",
                    "Shift-Cmd-Alt-F": "replaceAll",
                    "Cmd-[": "indentLess",
                    "Cmd-]": "indentMore",
                    "Cmd-Backspace": "delWrappedLineLeft",
                    "Cmd-Delete": "delWrappedLineRight",
                    "Cmd-U": "undoSelection",
                    "Shift-Cmd-U": "redoSelection",
                    "Ctrl-Up": "goDocStart",
                    "Ctrl-Down": "goDocEnd",
                    fallthrough: ["basic", "emacsy"]
                }, Il["default"] = y ? Il.macDefault : Il.pcDefault;
                var Xl = {
                    selectAll: Yo,
                    singleSelection: function(e) {
                        return e.setSelection(e.getCursor("anchor"), e.getCursor("head"), j)
                    },
                    killLine: function(e) {
                        return Gl(e, (function(t) {
                            if (t.empty()) {
                                var n = ue(e.doc, t.head.line).text.length;
                                return t.head.ch == n && t.head.line < e.lastLine() ? {
                                    from: t.head,
                                    to: me(t.head.line + 1, 0)
                                } : {
                                    from: t.head,
                                    to: me(t.head.line, n)
                                }
                            }
                            return {
                                from: t.from(),
                                to: t.to()
                            }
                        }))
                    },
                    deleteLine: function(e) {
                        return Gl(e, (function(t) {
                            return {
                                from: me(t.from().line, 0),
                                to: Se(e.doc, me(t.to().line + 1, 0))
                            }
                        }))
                    },
                    delLineLeft: function(e) {
                        return Gl(e, (function(e) {
                            return {
                                from: me(e.from().line, 0),
                                to: e.from()
                            }
                        }))
                    },
                    delWrappedLineLeft: function(e) {
                        return Gl(e, (function(t) {
                            var n = e.charCoords(t.head, "div").top + 5,
                                r = e.coordsChar({
                                    left: 0,
                                    top: n
                                }, "div");
                            return {
                                from: r,
                                to: t.from()
                            }
                        }))
                    },
                    delWrappedLineRight: function(e) {
                        return Gl(e, (function(t) {
                            var n = e.charCoords(t.head, "div").top + 5,
                                r = e.coordsChar({
                                    left: e.display.lineDiv.offsetWidth + 100,
                                    top: n
                                }, "div");
                            return {
                                from: t.from(),
                                to: r
                            }
                        }))
                    },
                    undo: function(e) {
                        return e.undo()
                    },
                    redo: function(e) {
                        return e.redo()
                    },
                    undoSelection: function(e) {
                        return e.undoSelection()
                    },
                    redoSelection: function(e) {
                        return e.redoSelection()
                    },
                    goDocStart: function(e) {
                        return e.extendSelection(me(e.firstLine(), 0))
                    },
                    goDocEnd: function(e) {
                        return e.extendSelection(me(e.lastLine()))
                    },
                    goLineStart: function(e) {
                        return e.extendSelectionsBy((function(t) {
                            return ql(e, t.head.line)
                        }), {
                            origin: "+move",
                            bias: 1
                        })
                    },
                    goLineStartSmart: function(e) {
                        return e.extendSelectionsBy((function(t) {
                            return Zl(e, t.head)
                        }), {
                            origin: "+move",
                            bias: 1
                        })
                    },
                    goLineEnd: function(e) {
                        return e.extendSelectionsBy((function(t) {
                            return Jl(e, t.head.line)
                        }), {
                            origin: "+move",
                            bias: -1
                        })
                    },
                    goLineRight: function(e) {
                        return e.extendSelectionsBy((function(t) {
                            var n = e.cursorCoords(t.head, "div").top + 5;
                            return e.coordsChar({
                                left: e.display.lineDiv.offsetWidth + 100,
                                top: n
                            }, "div")
                        }), V)
                    },
                    goLineLeft: function(e) {
                        return e.extendSelectionsBy((function(t) {
                            var n = e.cursorCoords(t.head, "div").top + 5;
                            return e.coordsChar({
                                left: 0,
                                top: n
                            }, "div")
                        }), V)
                    },
                    goLineLeftSmart: function(e) {
                        return e.extendSelectionsBy((function(t) {
                            var n = e.cursorCoords(t.head, "div").top + 5,
                                r = e.coordsChar({
                                    left: 0,
                                    top: n
                                }, "div");
                            return r.ch < e.getLine(r.line).search(/\S/) ? Zl(e, t.head) : r
                        }), V)
                    },
                    goLineUp: function(e) {
                        return e.moveV(-1, "line")
                    },
                    goLineDown: function(e) {
                        return e.moveV(1, "line")
                    },
                    goPageUp: function(e) {
                        return e.moveV(-1, "page")
                    },
                    goPageDown: function(e) {
                        return e.moveV(1, "page")
                    },
                    goCharLeft: function(e) {
                        return e.moveH(-1, "char")
                    },
                    goCharRight: function(e) {
                        return e.moveH(1, "char")
                    },
                    goColumnLeft: function(e) {
                        return e.moveH(-1, "column")
                    },
                    goColumnRight: function(e) {
                        return e.moveH(1, "column")
                    },
                    goWordLeft: function(e) {
                        return e.moveH(-1, "word")
                    },
                    goGroupRight: function(e) {
                        return e.moveH(1, "group")
                    },
                    goGroupLeft: function(e) {
                        return e.moveH(-1, "group")
                    },
                    goWordRight: function(e) {
                        return e.moveH(1, "word")
                    },
                    delCharBefore: function(e) {
                        return e.deleteH(-1, "char")
                    },
                    delCharAfter: function(e) {
                        return e.deleteH(1, "char")
                    },
                    delWordBefore: function(e) {
                        return e.deleteH(-1, "word")
                    },
                    delWordAfter: function(e) {
                        return e.deleteH(1, "word")
                    },
                    delGroupBefore: function(e) {
                        return e.deleteH(-1, "group")
                    },
                    delGroupAfter: function(e) {
                        return e.deleteH(1, "group")
                    },
                    indentAuto: function(e) {
                        return e.indentSelection("smart")
                    },
                    indentMore: function(e) {
                        return e.indentSelection("add")
                    },
                    indentLess: function(e) {
                        return e.indentSelection("subtract")
                    },
                    insertTab: function(e) {
                        return e.replaceSelection("\t")
                    },
                    insertSoftTab: function(e) {
                        for (var t = [], n = e.listSelections(), r = e.options.tabSize, i = 0; i < n.length; i++) {
                            var o = n[i].from(),
                                l = R(e.getLine(o.line), o.ch, r);
                            t.push(Y(r - l % r))
                        }
                        e.replaceSelections(t)
                    },
                    defaultTab: function(e) {
                        e.somethingSelected() ? e.indentSelection("add") : e.execCommand("insertTab")
                    },
                    transposeChars: function(e) {
                        return Mi(e, (function() {
                            for (var t = e.listSelections(), n = [], r = 0; r < t.length; r++)
                                if (t[r].empty()) {
                                    var i = t[r].head,
                                        o = ue(e.doc, i.line).text;
                                    if (o)
                                        if (i.ch == o.length && (i = new me(i.line, i.ch - 1)), i.ch > 0) i = new me(i.line, i.ch + 1), e.replaceRange(o.charAt(i.ch - 1) + o.charAt(i.ch - 2), me(i.line, i.ch - 2), i, "+transpose");
                                        else if (i.line > e.doc.first) {
                                        var l = ue(e.doc, i.line - 1).text;
                                        l && (i = new me(i.line, 1), e.replaceRange(o.charAt(0) + e.doc.lineSeparator() + l.charAt(l.length - 1), me(i.line - 1, l.length - 1), i, "+transpose"))
                                    }
                                    n.push(new ro(i, i))
                                } e.setSelections(n)
                        }))
                    },
                    newlineAndIndent: function(e) {
                        return Mi(e, (function() {
                            for (var t = e.listSelections(), n = t.length - 1; n >= 0; n--) e.replaceRange(e.doc.lineSeparator(), t[n].anchor, t[n].head, "+input");
                            t = e.listSelections();
                            for (var r = 0; r < t.length; r++) e.indentLine(t[r].from().line, null, !0);
                            ri(e)
                        }))
                    },
                    openLine: function(e) {
                        return e.replaceSelection("\n", "start")
                    },
                    toggleOverwrite: function(e) {
                        return e.toggleOverwrite()
                    }
                };

                function ql(e, t) {
                    var n = ue(e.doc, t),
                        r = qe(n);
                    return r != n && (t = de(r)), Kl(!0, e, r, t, 1)
                }

                function Jl(e, t) {
                    var n = ue(e.doc, t),
                        r = Je(n);
                    return r != n && (t = de(r)), Kl(!0, e, n, t, -1)
                }

                function Zl(e, t) {
                    var n = ql(e, t.line),
                        r = ue(e.doc, n.line),
                        i = ct(r, e.doc.direction);
                    if (!i || 0 == i[0].level) {
                        var o = Math.max(0, r.text.search(/\S/)),
                            l = t.line == n.line && t.ch <= o && t.ch;
                        return me(n.line, l ? 0 : o, n.sticky)
                    }
                    return n
                }

                function Ql(e, t, n) {
                    if ("string" == typeof t && (t = Xl[t], !t)) return !1;
                    e.display.input.ensurePolled();
                    var r = e.display.shift,
                        i = !1;
                    try {
                        e.isReadOnly() && (e.state.suppressEdits = !0), n && (e.display.shift = !1), i = t(e) != _
                    } finally {
                        e.display.shift = r, e.state.suppressEdits = !1
                    }
                    return i
                }

                function ea(e, t, n) {
                    for (var r = 0; r < e.state.keyMaps.length; r++) {
                        var i = zl(t, e.state.keyMaps[r], n, e);
                        if (i) return i
                    }
                    return e.options.extraKeys && zl(t, e.options.extraKeys, n, e) || zl(t, e.options.keyMap, n, e)
                }
                var ta = new z;

                function na(e, t, n, r) {
                    var i = e.state.keySeq;
                    if (i) {
                        if (Bl(t)) return "handled";
                        if (/\'$/.test(t) ? e.state.keySeq = null : ta.set(50, (function() {
                                e.state.keySeq == i && (e.state.keySeq = null, e.display.input.reset())
                            })), ra(e, i + " " + t, n, r)) return !0
                    }
                    return ra(e, t, n, r)
                }

                function ra(e, t, n, r) {
                    var i = ea(e, t, r);
                    return "multi" == i && (e.state.keySeq = t), "handled" == i && On(e, "keyHandled", e, t, n), "handled" != i && "multi" != i || (wt(n), _r(e)), !!i
                }

                function ia(e, t) {
                    var n = _l(t, !0);
                    return !!n && (t.shiftKey && !e.state.keySeq ? na(e, "Shift-" + n, t, (function(t) {
                        return Ql(e, t, !0)
                    })) || na(e, n, t, (function(t) {
                        if ("string" == typeof t ? /^go[A-Z]/.test(t) : t.motion) return Ql(e, t)
                    })) : na(e, n, t, (function(t) {
                        return Ql(e, t)
                    })))
                }

                function oa(e, t, n) {
                    return na(e, "'" + n + "'", t, (function(t) {
                        return Ql(e, t, !0)
                    }))
                }
                var la = null;

                function aa(e) {
                    var t = this;
                    if (t.curOp.focus = E(), !vt(t, e)) {
                        l && a < 11 && 27 == e.keyCode && (e.returnValue = !1);
                        var n = e.keyCode;
                        t.display.shift = 16 == n || e.shiftKey;
                        var r = ia(t, e);
                        f && (la = r ? n : null, r || 88 != n || Wt || !(y ? e.metaKey : e.ctrlKey) || t.replaceSelection("", null, "cut")), 18 != n || /\bCodeMirror-crosshair\b/.test(t.display.lineDiv.className) || sa(t)
                    }
                }

                function sa(e) {
                    var t = e.display.lineDiv;

                    function n(e) {
                        18 != e.keyCode && e.altKey || (T(t, "CodeMirror-crosshair"), pt(document, "keyup", n), pt(document, "mouseover", n))
                    }
                    W(t, "CodeMirror-crosshair"), ht(document, "keyup", n), ht(document, "mouseover", n)
                }

                function ua(e) {
                    16 == e.keyCode && (this.doc.sel.shift = !1), vt(this, e)
                }

                function ca(e) {
                    var t = this;
                    if (!(Gn(t.display, e) || vt(t, e) || e.ctrlKey && !e.altKey || y && e.metaKey)) {
                        var n = e.keyCode,
                            r = e.charCode;
                        if (f && n == la) return la = null, void wt(e);
                        if (!f || e.which && !(e.which < 10) || !ia(t, e)) {
                            var i = String.fromCharCode(null == r ? n : r);
                            "\b" != i && (oa(t, e, i) || t.display.input.onKeyPress(e))
                        }
                    }
                }
                var fa, ha, da = 400,
                    pa = function(e, t, n) {
                        this.time = e, this.pos = t, this.button = n
                    };

                function ga(e, t) {
                    var n = +new Date;
                    return ha && ha.compare(n, e, t) ? (fa = ha = null, "triple") : fa && fa.compare(n, e, t) ? (ha = new pa(n, e, t), fa = null, "double") : (fa = new pa(n, e, t), ha = null, "single")
                }

                function va(e) {
                    var t = this,
                        n = t.display;
                    if (!(vt(t, e) || n.activeTouch && n.input.supportsTouch()))
                        if (n.input.ensurePolled(), n.shift = e.shiftKey, Gn(n, e)) s || (n.scroller.draggable = !1, setTimeout((function() {
                            return n.scroller.draggable = !0
                        }), 100));
                        else if (!La(t, e)) {
                        var r = Fr(t, e),
                            i = Lt(e),
                            o = r ? ga(r, i) : "single";
                        window.focus(), 1 == i && t.state.selectingText && t.state.selectingText(e), r && ma(t, i, r, o, e) || (1 == i ? r ? ba(t, r, o, e) : St(e) == n.scroller && wt(e) : 2 == i ? (r && Ho(t.doc, r), setTimeout((function() {
                            return n.input.focus()
                        }), 20)) : 3 == i && (C ? t.display.input.onContextMenu(e) : Gr(t)))
                    }
                }

                function ma(e, t, n, r, i) {
                    var o = "Click";
                    return "double" == r ? o = "Double" + o : "triple" == r && (o = "Triple" + o), o = (1 == t ? "Left" : 2 == t ? "Middle" : "Right") + o, na(e, $l(o, i), i, (function(t) {
                        if ("string" == typeof t && (t = Xl[t]), !t) return !1;
                        var r = !1;
                        try {
                            e.isReadOnly() && (e.state.suppressEdits = !0), r = t(e, n) != _
                        } finally {
                            e.state.suppressEdits = !1
                        }
                        return r
                    }))
                }

                function ya(e, t, n) {
                    var r = e.getOption("configureMouse"),
                        i = r ? r(e, t, n) : {};
                    if (null == i.unit) {
                        var o = b ? n.shiftKey && n.metaKey : n.altKey;
                        i.unit = o ? "rectangle" : "single" == t ? "char" : "double" == t ? "word" : "line"
                    }
                    return (null == i.extend || e.doc.extend) && (i.extend = e.doc.extend || n.shiftKey), null == i.addNew && (i.addNew = y ? n.metaKey : n.ctrlKey), null == i.moveOnDrag && (i.moveOnDrag = !(y ? n.altKey : n.ctrlKey)), i
                }

                function ba(e, t, n, r) {
                    l ? setTimeout(I(jr, e), 0) : e.curOp.focus = E();
                    var i, o = ya(e, n, r),
                        a = e.doc.sel;
                    e.options.dragDrop && Nt && !e.isReadOnly() && "single" == n && (i = a.contains(t)) > -1 && (ye((i = a.ranges[i]).from(), t) < 0 || t.xRel > 0) && (ye(i.to(), t) > 0 || t.xRel < 0) ? wa(e, r, t, o) : ka(e, r, t, o)
                }

                function wa(e, t, n, r) {
                    var i = e.display,
                        o = !1,
                        u = Ni(e, (function(t) {
                            s && (i.scroller.draggable = !1), e.state.draggingText = !1, pt(i.wrapper.ownerDocument, "mouseup", u), pt(i.wrapper.ownerDocument, "mousemove", c), pt(i.scroller, "dragstart", f), pt(i.scroller, "drop", u), o || (wt(t), r.addNew || Ho(e.doc, n, null, null, r.extend), s || l && 9 == a ? setTimeout((function() {
                                i.wrapper.ownerDocument.body.focus(), i.input.focus()
                            }), 20) : i.input.focus())
                        })),
                        c = function(e) {
                            o = o || Math.abs(t.clientX - e.clientX) + Math.abs(t.clientY - e.clientY) >= 10
                        },
                        f = function() {
                            return o = !0
                        };
                    s && (i.scroller.draggable = !0), e.state.draggingText = u, u.copy = !r.moveOnDrag, i.scroller.dragDrop && i.scroller.dragDrop(), ht(i.wrapper.ownerDocument, "mouseup", u), ht(i.wrapper.ownerDocument, "mousemove", c), ht(i.scroller, "dragstart", f), ht(i.scroller, "drop", u), Gr(e), setTimeout((function() {
                        return i.input.focus()
                    }), 20)
                }

                function xa(e, t, n) {
                    if ("char" == n) return new ro(t, t);
                    if ("word" == n) return e.findWordAt(t);
                    if ("line" == n) return new ro(me(t.line, 0), Se(e.doc, me(t.line + 1, 0)));
                    var r = n(e, t);
                    return new ro(r.from, r.to)
                }

                function ka(e, t, n, r) {
                    var i = e.display,
                        o = e.doc;
                    wt(t);
                    var l, a, s = o.sel,
                        u = s.ranges;
                    if (r.addNew && !r.extend ? (a = o.sel.contains(n), l = a > -1 ? u[a] : new ro(n, n)) : (l = o.sel.primary(), a = o.sel.primIndex), "rectangle" == r.unit) r.addNew || (l = new ro(n, n)), n = Fr(e, t, !0, !0), a = -1;
                    else {
                        var c = xa(e, n, r.unit);
                        l = r.extend ? Wo(l, c.anchor, c.head, r.extend) : c
                    }
                    r.addNew ? -1 == a ? (a = u.length, Bo(o, io(e, u.concat([l]), a), {
                        scroll: !1,
                        origin: "*mouse"
                    })) : u.length > 1 && u[a].empty() && "char" == r.unit && !r.extend ? (Bo(o, io(e, u.slice(0, a).concat(u.slice(a + 1)), 0), {
                        scroll: !1,
                        origin: "*mouse"
                    }), s = o.sel) : Io(o, a, l, G) : (a = 0, Bo(o, new no([l], 0), G), s = o.sel);
                    var f = n;

                    function h(t) {
                        if (0 != ye(f, t))
                            if (f = t, "rectangle" == r.unit) {
                                for (var i = [], u = e.options.tabSize, c = R(ue(o, n.line).text, n.ch, u), h = R(ue(o, t.line).text, t.ch, u), d = Math.min(c, h), p = Math.max(c, h), g = Math.min(n.line, t.line), v = Math.min(e.lastLine(), Math.max(n.line, t.line)); g <= v; g++) {
                                    var m = ue(o, g).text,
                                        y = U(m, d, u);
                                    d == p ? i.push(new ro(me(g, y), me(g, y))) : m.length > y && i.push(new ro(me(g, y), me(g, U(m, p, u))))
                                }
                                i.length || i.push(new ro(n, n)), Bo(o, io(e, s.ranges.slice(0, a).concat(i), a), {
                                    origin: "*mouse",
                                    scroll: !1
                                }), e.scrollIntoView(t)
                            } else {
                                var b, w = l,
                                    x = xa(e, t, r.unit),
                                    k = w.anchor;
                                ye(x.anchor, k) > 0 ? (b = x.head, k = ke(w.from(), x.anchor)) : (b = x.anchor, k = xe(w.to(), x.head));
                                var C = s.ranges.slice(0);
                                C[a] = Ca(e, new ro(Se(o, k), b)), Bo(o, io(e, C, a), G)
                            }
                    }
                    var d = i.wrapper.getBoundingClientRect(),
                        p = 0;

                    function g(t) {
                        var n = ++p,
                            l = Fr(e, t, !0, "rectangle" == r.unit);
                        if (l)
                            if (0 != ye(l, f)) {
                                e.curOp.focus = E(), h(l);
                                var a = Xr(i, o);
                                (l.line >= a.to || l.line < a.from) && setTimeout(Ni(e, (function() {
                                    p == n && g(t)
                                })), 150)
                            } else {
                                var s = t.clientY < d.top ? -20 : t.clientY > d.bottom ? 20 : 0;
                                s && setTimeout(Ni(e, (function() {
                                    p == n && (i.scroller.scrollTop += s, g(t))
                                })), 50)
                            }
                    }

                    function v(t) {
                        e.state.selectingText = !1, p = 1 / 0, wt(t), i.input.focus(), pt(i.wrapper.ownerDocument, "mousemove", m), pt(i.wrapper.ownerDocument, "mouseup", y), o.history.lastSelOrigin = null
                    }
                    var m = Ni(e, (function(e) {
                            0 !== e.buttons && Lt(e) ? g(e) : v(e)
                        })),
                        y = Ni(e, v);
                    e.state.selectingText = y, ht(i.wrapper.ownerDocument, "mousemove", m), ht(i.wrapper.ownerDocument, "mouseup", y)
                }

                function Ca(e, t) {
                    var n = t.anchor,
                        r = t.head,
                        i = ue(e.doc, n.line);
                    if (0 == ye(n, r) && n.sticky == r.sticky) return t;
                    var o = ct(i);
                    if (!o) return t;
                    var l = st(o, n.ch, n.sticky),
                        a = o[l];
                    if (a.from != n.ch && a.to != n.ch) return t;
                    var s, u = l + (a.from == n.ch == (1 != a.level) ? 0 : 1);
                    if (0 == u || u == o.length) return t;
                    if (r.line != n.line) s = (r.line - n.line) * ("ltr" == e.doc.direction ? 1 : -1) > 0;
                    else {
                        var c = st(o, r.ch, r.sticky),
                            f = c - l || (r.ch - n.ch) * (1 == a.level ? -1 : 1);
                        s = c == u - 1 || c == u ? f < 0 : f > 0
                    }
                    var h = o[u + (s ? -1 : 0)],
                        d = s == (1 == h.level),
                        p = d ? h.from : h.to,
                        g = d ? "after" : "before";
                    return n.ch == p && n.sticky == g ? t : new ro(new me(n.line, p, g), r)
                }

                function Sa(e, t, n, r) {
                    var i, o;
                    if (t.touches) i = t.touches[0].clientX, o = t.touches[0].clientY;
                    else try {
                        i = t.clientX, o = t.clientY
                    } catch (t) {
                        return !1
                    }
                    if (i >= Math.floor(e.display.gutters.getBoundingClientRect().right)) return !1;
                    r && wt(t);
                    var l = e.display,
                        a = l.lineDiv.getBoundingClientRect();
                    if (o > a.bottom || !yt(e, n)) return kt(t);
                    o -= a.top - l.viewOffset;
                    for (var s = 0; s < e.options.gutters.length; ++s) {
                        var u = l.gutters.childNodes[s];
                        if (u && u.getBoundingClientRect().right >= i) {
                            var c = pe(e.doc, o),
                                f = e.options.gutters[s];
                            return gt(e, n, e, c, f, t), kt(t)
                        }
                    }
                }

                function La(e, t) {
                    return Sa(e, t, "gutterClick", !0)
                }

                function Ta(e, t) {
                    Gn(e.display, t) || Ma(e, t) || vt(e, t, "contextmenu") || C || e.display.input.onContextMenu(t)
                }

                function Ma(e, t) {
                    return !!yt(e, "gutterContextMenu") && Sa(e, t, "gutterContextMenu", !1)
                }

                function Na(e) {
                    e.display.wrapper.className = e.display.wrapper.className.replace(/\s*cm-s-\S+/g, "") + e.options.theme.replace(/(^|\s)\s*/g, " cm-s-"), hr(e)
                }
                pa.prototype.compare = function(e, t, n) {
                    return this.time + da > e && 0 == ye(t, this.pos) && n == this.button
                };
                var Oa = {
                        toString: function() {
                            return "CodeMirror.Init"
                        }
                    },
                    Aa = {},
                    Da = {};

                function Ea(e) {
                    var t = e.optionHandlers;

                    function n(n, r, i, o) {
                        e.defaults[n] = r, i && (t[n] = o ? function(e, t, n) {
                            n != Oa && i(e, t, n)
                        } : i)
                    }
                    e.defineOption = n, e.Init = Oa, n("value", "", (function(e, t) {
                        return e.setValue(t)
                    }), !0), n("mode", null, (function(e, t) {
                        e.doc.modeOption = t, fo(e)
                    }), !0), n("indentUnit", 2, fo, !0), n("indentWithTabs", !1), n("smartIndent", !0), n("tabSize", 4, (function(e) {
                        ho(e), hr(e), Di(e)
                    }), !0), n("lineSeparator", null, (function(e, t) {
                        if (e.doc.lineSep = t, t) {
                            var n = [],
                                r = e.doc.first;
                            e.doc.iter((function(e) {
                                for (var i = 0;;) {
                                    var o = e.text.indexOf(t, i);
                                    if (-1 == o) break;
                                    i = o + t.length, n.push(me(r, o))
                                }
                                r++
                            }));
                            for (var i = n.length - 1; i >= 0; i--) nl(e.doc, t, n[i], me(n[i].line, n[i].ch + t.length))
                        }
                    })), n("specialChars", /[\u0000-\u001f\u007f-\u009f\u00ad\u061c\u200b-\u200f\u2028\u2029\ufeff]/g, (function(e, t, n) {
                        e.state.specialChars = new RegExp(t.source + (t.test("\t") ? "" : "|\t"), "g"), n != Oa && e.refresh()
                    })), n("specialCharPlaceholder", vn, (function(e) {
                        return e.refresh()
                    }), !0), n("electricChars", !0), n("inputStyle", m ? "contenteditable" : "textarea", (function() {
                        throw new Error("inputStyle can not (yet) be changed in a running editor")
                    }), !0), n("spellcheck", !1, (function(e, t) {
                        return e.getInputField().spellcheck = t
                    }), !0), n("autocorrect", !1, (function(e, t) {
                        return e.getInputField().autocorrect = t
                    }), !0), n("autocapitalize", !1, (function(e, t) {
                        return e.getInputField().autocapitalize = t
                    }), !0), n("rtlMoveVisually", !w), n("wholeLineUpdateBefore", !0), n("theme", "default", (function(e) {
                        Na(e), Wa(e)
                    }), !0), n("keyMap", "default", (function(e, t, n) {
                        var r = jl(t),
                            i = n != Oa && jl(n);
                        i && i.detach && i.detach(e, r), r.attach && r.attach(e, i || null)
                    })), n("extraKeys", null), n("configureMouse", null), n("lineWrapping", !1, Fa, !0), n("gutters", [], (function(e) {
                        qi(e.options), Wa(e)
                    }), !0), n("fixedGutter", !0, (function(e, t) {
                        e.display.gutters.style.left = t ? Er(e.display) + "px" : "0", e.refresh()
                    }), !0), n("coverGutterNextToScrollbar", !1, (function(e) {
                        return pi(e)
                    }), !0), n("scrollbarStyle", "native", (function(e) {
                        mi(e), pi(e), e.display.scrollbars.setScrollTop(e.doc.scrollTop), e.display.scrollbars.setScrollLeft(e.doc.scrollLeft)
                    }), !0), n("lineNumbers", !1, (function(e) {
                        qi(e.options), Wa(e)
                    }), !0), n("firstLineNumber", 1, Wa, !0), n("lineNumberFormatter", (function(e) {
                        return e
                    }), Wa, !0), n("showCursorWhenSelecting", !1, Pr, !0), n("resetSelectionOnContextMenu", !0), n("lineWiseCopyCut", !0), n("pasteLinesPerSelection", !0), n("selectionsMayTouch", !1), n("readOnly", !1, (function(e, t) {
                        "nocursor" == t && (Ur(e), e.display.input.blur()), e.display.input.readOnlyChanged(t)
                    })), n("disableInput", !1, (function(e, t) {
                        t || e.display.input.reset()
                    }), !0), n("dragDrop", !0, Ha), n("allowDropFileTypes", null), n("cursorBlinkRate", 530), n("cursorScrollMargin", 0), n("cursorHeight", 1, Pr, !0), n("singleCursorHeightPerLine", !0, Pr, !0), n("workTime", 100), n("workDelay", 100), n("flattenSpans", !0, ho, !0), n("addModeClass", !1, ho, !0), n("pollInterval", 100), n("undoDepth", 200, (function(e, t) {
                        return e.doc.history.undoDepth = t
                    })), n("historyEventDelay", 1250), n("viewportMargin", 10, (function(e) {
                        return e.refresh()
                    }), !0), n("maxHighlightLength", 1e4, ho, !0), n("moveInputWithCursor", !0, (function(e, t) {
                        t || e.display.input.resetPosition()
                    })), n("tabindex", null, (function(e, t) {
                        return e.display.input.getField().tabIndex = t || ""
                    })), n("autofocus", null), n("direction", "ltr", (function(e, t) {
                        return e.doc.setDirection(t)
                    }), !0), n("phrases", null)
                }

                function Wa(e) {
                    Xi(e), Di(e), qr(e)
                }

                function Ha(e, t, n) {
                    var r = n && n != Oa;
                    if (!t != !r) {
                        var i = e.display.dragFunctions,
                            o = t ? ht : pt;
                        o(e.display.scroller, "dragstart", i.start), o(e.display.scroller, "dragenter", i.enter), o(e.display.scroller, "dragover", i.over), o(e.display.scroller, "dragleave", i.leave), o(e.display.scroller, "drop", i.drop)
                    }
                }

                function Fa(e) {
                    e.options.lineWrapping ? (W(e.display.wrapper, "CodeMirror-wrap"), e.display.sizer.style.minWidth = "", e.display.sizerWidth = null) : (T(e.display.wrapper, "CodeMirror-wrap"), ot(e)), Hr(e), Di(e), hr(e), setTimeout((function() {
                        return pi(e)
                    }), 100)
                }

                function Ia(e, t) {
                    var n = this;
                    if (!(this instanceof Ia)) return new Ia(e, t);
                    this.options = t = t ? P(t) : {}, P(Aa, t, !1), qi(t);
                    var r = t.value;
                    "string" == typeof r ? r = new xl(r, t.mode, null, t.lineSeparator, t.direction) : t.mode && (r.modeOption = t.mode), this.doc = r;
                    var i = new Ia.inputStyles[t.inputStyle](this),
                        o = this.display = new se(e, r, i);
                    for (var u in o.wrapper.CodeMirror = this, Xi(this), Na(this), t.lineWrapping && (this.display.wrapper.className += " CodeMirror-wrap"), mi(this), this.state = {
                            keyMaps: [],
                            overlays: [],
                            modeGen: 0,
                            overwrite: !1,
                            delayingBlurEvent: !1,
                            focused: !1,
                            suppressEdits: !1,
                            pasteIncoming: -1,
                            cutIncoming: -1,
                            selectingText: !1,
                            draggingText: !1,
                            highlight: new z,
                            keySeq: null,
                            specialChars: null
                        }, t.autofocus && !m && o.input.focus(), l && a < 11 && setTimeout((function() {
                            return n.display.input.reset(!0)
                        }), 20), Pa(this), Ol(), bi(this), this.curOp.forceUpdate = !0, mo(this, r), t.autofocus && !m || this.hasFocus() ? setTimeout(I(Vr, this), 20) : Ur(this), Da) Da.hasOwnProperty(u) && Da[u](n, t[u], Oa);
                    Jr(this), t.finishInit && t.finishInit(this);
                    for (var c = 0; c < Ra.length; ++c) Ra[c](n);
                    wi(this), s && t.lineWrapping && "optimizelegibility" == getComputedStyle(o.lineDiv).textRendering && (o.lineDiv.style.textRendering = "auto")
                }

                function Pa(e) {
                    var t = e.display;
                    ht(t.scroller, "mousedown", Ni(e, va)), ht(t.scroller, "dblclick", l && a < 11 ? Ni(e, (function(t) {
                        if (!vt(e, t)) {
                            var n = Fr(e, t);
                            if (n && !La(e, t) && !Gn(e.display, t)) {
                                wt(t);
                                var r = e.findWordAt(n);
                                Ho(e.doc, r.anchor, r.head)
                            }
                        }
                    })) : function(t) {
                        return vt(e, t) || wt(t)
                    }), ht(t.scroller, "contextmenu", (function(t) {
                        return Ta(e, t)
                    }));
                    var n, r = {
                        end: 0
                    };

                    function i() {
                        t.activeTouch && (n = setTimeout((function() {
                            return t.activeTouch = null
                        }), 1e3), r = t.activeTouch, r.end = +new Date)
                    }

                    function o(e) {
                        if (1 != e.touches.length) return !1;
                        var t = e.touches[0];
                        return t.radiusX <= 1 && t.radiusY <= 1
                    }

                    function s(e, t) {
                        if (null == t.left) return !0;
                        var n = t.left - e.left,
                            r = t.top - e.top;
                        return n * n + r * r > 400
                    }
                    ht(t.scroller, "touchstart", (function(i) {
                        if (!vt(e, i) && !o(i) && !La(e, i)) {
                            t.input.ensurePolled(), clearTimeout(n);
                            var l = +new Date;
                            t.activeTouch = {
                                start: l,
                                moved: !1,
                                prev: l - r.end <= 300 ? r : null
                            }, 1 == i.touches.length && (t.activeTouch.left = i.touches[0].pageX, t.activeTouch.top = i.touches[0].pageY)
                        }
                    })), ht(t.scroller, "touchmove", (function() {
                        t.activeTouch && (t.activeTouch.moved = !0)
                    })), ht(t.scroller, "touchend", (function(n) {
                        var r = t.activeTouch;
                        if (r && !Gn(t, n) && null != r.left && !r.moved && new Date - r.start < 300) {
                            var o, l = e.coordsChar(t.activeTouch, "page");
                            o = !r.prev || s(r, r.prev) ? new ro(l, l) : !r.prev.prev || s(r, r.prev.prev) ? e.findWordAt(l) : new ro(me(l.line, 0), Se(e.doc, me(l.line + 1, 0))), e.setSelection(o.anchor, o.head), e.focus(), wt(n)
                        }
                        i()
                    })), ht(t.scroller, "touchcancel", i), ht(t.scroller, "scroll", (function() {
                        t.scroller.clientHeight && (si(e, t.scroller.scrollTop), ci(e, t.scroller.scrollLeft, !0), gt(e, "scroll", e))
                    })), ht(t.scroller, "mousewheel", (function(t) {
                        return to(e, t)
                    })), ht(t.scroller, "DOMMouseScroll", (function(t) {
                        return to(e, t)
                    })), ht(t.wrapper, "scroll", (function() {
                        return t.wrapper.scrollTop = t.wrapper.scrollLeft = 0
                    })), t.dragFunctions = {
                        enter: function(t) {
                            vt(e, t) || Ct(t)
                        },
                        over: function(t) {
                            vt(e, t) || (Ll(e, t), Ct(t))
                        },
                        start: function(t) {
                            return Sl(e, t)
                        },
                        drop: Ni(e, Cl),
                        leave: function(t) {
                            vt(e, t) || Tl(e)
                        }
                    };
                    var u = t.input.getField();
                    ht(u, "keyup", (function(t) {
                        return ua.call(e, t)
                    })), ht(u, "keydown", Ni(e, aa)), ht(u, "keypress", Ni(e, ca)), ht(u, "focus", (function(t) {
                        return Vr(e, t)
                    })), ht(u, "blur", (function(t) {
                        return Ur(e, t)
                    }))
                }
                Ia.defaults = Aa, Ia.optionHandlers = Da;
                var Ra = [];

                function za(e, t, n, r) {
                    var i, o = e.doc;
                    null == n && (n = "add"), "smart" == n && (o.mode.indent ? i = Zt(e, t).state : n = "prev");
                    var l = e.options.tabSize,
                        a = ue(o, t),
                        s = R(a.text, null, l);
                    a.stateAfter && (a.stateAfter = null);
                    var u, c = a.text.match(/^\s*/)[0];
                    if (r || /\S/.test(a.text)) {
                        if ("smart" == n && (u = o.mode.indent(i, a.text.slice(c.length), a.text), u == _ || u > 150)) {
                            if (!r) return;
                            n = "prev"
                        }
                    } else u = 0, n = "not";
                    "prev" == n ? u = t > o.first ? R(ue(o, t - 1).text, null, l) : 0 : "add" == n ? u = s + e.options.indentUnit : "subtract" == n ? u = s - e.options.indentUnit : "number" == typeof n && (u = s + n), u = Math.max(0, u);
                    var f = "",
                        h = 0;
                    if (e.options.indentWithTabs)
                        for (var d = Math.floor(u / l); d; --d) h += l, f += "\t";
                    if (h < u && (f += Y(u - h)), f != c) return nl(o, f, me(t, 0), me(t, c.length), "+input"), a.stateAfter = null, !0;
                    for (var p = 0; p < o.sel.ranges.length; p++) {
                        var g = o.sel.ranges[p];
                        if (g.head.line == t && g.head.ch < c.length) {
                            var v = me(t, c.length);
                            Io(o, p, new ro(v, v));
                            break
                        }
                    }
                }
                Ia.defineInitHook = function(e) {
                    return Ra.push(e)
                };
                var Ba = null;

                function $a(e) {
                    Ba = e
                }

                function _a(e, t, n, r, i) {
                    var o = e.doc;
                    e.display.shift = !1, r || (r = o.sel);
                    var l = +new Date - 200,
                        a = "paste" == i || e.state.pasteIncoming > l,
                        s = Dt(t),
                        u = null;
                    if (a && r.ranges.length > 1)
                        if (Ba && Ba.text.join("\n") == t) {
                            if (r.ranges.length % Ba.text.length == 0) {
                                u = [];
                                for (var c = 0; c < Ba.text.length; c++) u.push(o.splitLines(Ba.text[c]))
                            }
                        } else s.length == r.ranges.length && e.options.pasteLinesPerSelection && (u = q(s, (function(e) {
                            return [e]
                        })));
                    for (var f = e.curOp.updateInput, h = r.ranges.length - 1; h >= 0; h--) {
                        var d = r.ranges[h],
                            p = d.from(),
                            g = d.to();
                        d.empty() && (n && n > 0 ? p = me(p.line, p.ch - n) : e.state.overwrite && !a ? g = me(g.line, Math.min(ue(o, g.line).text.length, g.ch + X(s).length)) : a && Ba && Ba.lineWise && Ba.text.join("\n") == t && (p = g = me(p.line, 0)));
                        var v = {
                            from: p,
                            to: g,
                            text: u ? u[h % u.length] : s,
                            origin: i || (a ? "paste" : e.state.cutIncoming > l ? "cut" : "+input")
                        };
                        qo(e.doc, v), On(e, "inputRead", e, v)
                    }
                    t && !a && Ga(e, t), ri(e), e.curOp.updateInput < 2 && (e.curOp.updateInput = f), e.curOp.typing = !0, e.state.pasteIncoming = e.state.cutIncoming = -1
                }

                function ja(e, t) {
                    var n = e.clipboardData && e.clipboardData.getData("Text");
                    if (n) return e.preventDefault(), t.isReadOnly() || t.options.disableInput || Mi(t, (function() {
                        return _a(t, n, 0, null, "paste")
                    })), !0
                }

                function Ga(e, t) {
                    if (e.options.electricChars && e.options.smartIndent)
                        for (var n = e.doc.sel, r = n.ranges.length - 1; r >= 0; r--) {
                            var i = n.ranges[r];
                            if (!(i.head.ch > 100 || r && n.ranges[r - 1].head.line == i.head.line)) {
                                var o = e.getModeAt(i.head),
                                    l = !1;
                                if (o.electricChars) {
                                    for (var a = 0; a < o.electricChars.length; a++)
                                        if (t.indexOf(o.electricChars.charAt(a)) > -1) {
                                            l = za(e, i.head.line, "smart");
                                            break
                                        }
                                } else o.electricInput && o.electricInput.test(ue(e.doc, i.head.line).text.slice(0, i.head.ch)) && (l = za(e, i.head.line, "smart"));
                                l && On(e, "electricInput", e, i.head.line)
                            }
                        }
                }

                function Va(e) {
                    for (var t = [], n = [], r = 0; r < e.doc.sel.ranges.length; r++) {
                        var i = e.doc.sel.ranges[r].head.line,
                            o = {
                                anchor: me(i, 0),
                                head: me(i + 1, 0)
                            };
                        n.push(o), t.push(e.getRange(o.anchor, o.head))
                    }
                    return {
                        text: t,
                        ranges: n
                    }
                }

                function Ua(e, t, n, r) {
                    e.setAttribute("autocorrect", !!n), e.setAttribute("autocapitalize", !!r), e.setAttribute("spellcheck", !!t)
                }

                function Ka() {
                    var e = O("textarea", null, null, "position: absolute; bottom: -1em; padding: 0; width: 1px; height: 1em; outline: none"),
                        t = O("div", [e], null, "overflow: hidden; position: relative; width: 3px; height: 0px;");
                    return s ? e.style.width = "1000px" : e.setAttribute("wrap", "off"), g && (e.style.border = "1px solid black"), Ua(e), t
                }

                function Ya(e) {
                    var t = e.optionHandlers,
                        n = e.helpers = {};
                    e.prototype = {
                        constructor: e,
                        focus: function() {
                            window.focus(), this.display.input.focus()
                        },
                        setOption: function(e, n) {
                            var r = this.options,
                                i = r[e];
                            r[e] == n && "mode" != e || (r[e] = n, t.hasOwnProperty(e) && Ni(this, t[e])(this, n, i), gt(this, "optionChange", this, e))
                        },
                        getOption: function(e) {
                            return this.options[e]
                        },
                        getDoc: function() {
                            return this.doc
                        },
                        addKeyMap: function(e, t) {
                            this.state.keyMaps[t ? "push" : "unshift"](jl(e))
                        },
                        removeKeyMap: function(e) {
                            for (var t = this.state.keyMaps, n = 0; n < t.length; ++n)
                                if (t[n] == e || t[n].name == e) return t.splice(n, 1), !0
                        },
                        addOverlay: Oi((function(t, n) {
                            var r = t.token ? t : e.getMode(this.options, t);
                            if (r.startState) throw new Error("Overlays may not be stateful.");
                            J(this.state.overlays, {
                                mode: r,
                                modeSpec: t,
                                opaque: n && n.opaque,
                                priority: n && n.priority || 0
                            }, (function(e) {
                                return e.priority
                            })), this.state.modeGen++, Di(this)
                        })),
                        removeOverlay: Oi((function(e) {
                            for (var t = this, n = this.state.overlays, r = 0; r < n.length; ++r) {
                                var i = n[r].modeSpec;
                                if (i == e || "string" == typeof e && i.name == e) return n.splice(r, 1), t.state.modeGen++, void Di(t)
                            }
                        })),
                        indentLine: Oi((function(e, t, n) {
                            "string" != typeof t && "number" != typeof t && (t = null == t ? this.options.smartIndent ? "smart" : "prev" : t ? "add" : "subtract"), ge(this.doc, e) && za(this, e, t, n)
                        })),
                        indentSelection: Oi((function(e) {
                            for (var t = this, n = this.doc.sel.ranges, r = -1, i = 0; i < n.length; i++) {
                                var o = n[i];
                                if (o.empty()) o.head.line > r && (za(t, o.head.line, e, !0), r = o.head.line, i == t.doc.sel.primIndex && ri(t));
                                else {
                                    var l = o.from(),
                                        a = o.to(),
                                        s = Math.max(r, l.line);
                                    r = Math.min(t.lastLine(), a.line - (a.ch ? 0 : 1)) + 1;
                                    for (var u = s; u < r; ++u) za(t, u, e);
                                    var c = t.doc.sel.ranges;
                                    0 == l.ch && n.length == c.length && c[i].from().ch > 0 && Io(t.doc, i, new ro(l, c[i].to()), j)
                                }
                            }
                        })),
                        getTokenAt: function(e, t) {
                            return rn(this, e, t)
                        },
                        getLineTokens: function(e, t) {
                            return rn(this, me(e), t, !0)
                        },
                        getTokenTypeAt: function(e) {
                            e = Se(this.doc, e);
                            var t, n = Jt(this, ue(this.doc, e.line)),
                                r = 0,
                                i = (n.length - 1) / 2,
                                o = e.ch;
                            if (0 == o) t = n[2];
                            else
                                for (;;) {
                                    var l = r + i >> 1;
                                    if ((l ? n[2 * l - 1] : 0) >= o) i = l;
                                    else {
                                        if (!(n[2 * l + 1] < o)) {
                                            t = n[2 * l + 2];
                                            break
                                        }
                                        r = l + 1
                                    }
                                }
                            var a = t ? t.indexOf("overlay ") : -1;
                            return a < 0 ? t : 0 == a ? null : t.slice(0, a - 1)
                        },
                        getModeAt: function(t) {
                            var n = this.doc.mode;
                            return n.innerMode ? e.innerMode(n, this.getTokenAt(t).state).mode : n
                        },
                        getHelper: function(e, t) {
                            return this.getHelpers(e, t)[0]
                        },
                        getHelpers: function(e, t) {
                            var r = this,
                                i = [];
                            if (!n.hasOwnProperty(t)) return i;
                            var o = n[t],
                                l = this.getModeAt(e);
                            if ("string" == typeof l[t]) o[l[t]] && i.push(o[l[t]]);
                            else if (l[t])
                                for (var a = 0; a < l[t].length; a++) {
                                    var s = o[l[t][a]];
                                    s && i.push(s)
                                } else l.helperType && o[l.helperType] ? i.push(o[l.helperType]) : o[l.name] && i.push(o[l.name]);
                            for (var u = 0; u < o._global.length; u++) {
                                var c = o._global[u];
                                c.pred(l, r) && -1 == B(i, c.val) && i.push(c.val)
                            }
                            return i
                        },
                        getStateAfter: function(e, t) {
                            var n = this.doc;
                            return e = Ce(n, null == e ? n.first + n.size - 1 : e), Zt(this, e + 1, t).state
                        },
                        cursorCoords: function(e, t) {
                            var n, r = this.doc.sel.primary();
                            return n = null == e ? r.head : "object" == typeof e ? Se(this.doc, e) : e ? r.from() : r.to(), br(this, n, t || "page")
                        },
                        charCoords: function(e, t) {
                            return yr(this, Se(this.doc, e), t || "page")
                        },
                        coordsChar: function(e, t) {
                            return e = mr(this, e, t || "page"), kr(this, e.left, e.top)
                        },
                        lineAtHeight: function(e, t) {
                            return e = mr(this, {
                                top: e,
                                left: 0
                            }, t || "page").top, pe(this.doc, e + this.display.viewOffset)
                        },
                        heightAtLine: function(e, t, n) {
                            var r, i = !1;
                            if ("number" == typeof e) {
                                var o = this.doc.first + this.doc.size - 1;
                                e < this.doc.first ? e = this.doc.first : e > o && (e = o, i = !0), r = ue(this.doc, e)
                            } else r = e;
                            return vr(this, r, {
                                top: 0,
                                left: 0
                            }, t || "page", n || i).top + (i ? this.doc.height - rt(r) : 0)
                        },
                        defaultTextHeight: function() {
                            return Or(this.display)
                        },
                        defaultCharWidth: function() {
                            return Ar(this.display)
                        },
                        getViewport: function() {
                            return {
                                from: this.display.viewFrom,
                                to: this.display.viewTo
                            }
                        },
                        addWidget: function(e, t, n, r, i) {
                            var o = this.display;
                            e = br(this, Se(this.doc, e));
                            var l = e.bottom,
                                a = e.left;
                            if (t.style.position = "absolute", t.setAttribute("cm-ignore-events", "true"), this.display.input.setUneditable(t), o.sizer.appendChild(t), "over" == r) l = e.top;
                            else if ("above" == r || "near" == r) {
                                var s = Math.max(o.wrapper.clientHeight, this.doc.height),
                                    u = Math.max(o.sizer.clientWidth, o.lineSpace.clientWidth);
                                ("above" == r || e.bottom + t.offsetHeight > s) && e.top > t.offsetHeight ? l = e.top - t.offsetHeight : e.bottom + t.offsetHeight <= s && (l = e.bottom), a + t.offsetWidth > u && (a = u - t.offsetWidth)
                            }
                            t.style.top = l + "px", t.style.left = t.style.right = "", "right" == i ? (a = o.sizer.clientWidth - t.offsetWidth, t.style.right = "0px") : ("left" == i ? a = 0 : "middle" == i && (a = (o.sizer.clientWidth - t.offsetWidth) / 2), t.style.left = a + "px"), n && ei(this, {
                                left: a,
                                top: l,
                                right: a + t.offsetWidth,
                                bottom: l + t.offsetHeight
                            })
                        },
                        triggerOnKeyDown: Oi(aa),
                        triggerOnKeyPress: Oi(ca),
                        triggerOnKeyUp: ua,
                        triggerOnMouseDown: Oi(va),
                        execCommand: function(e) {
                            if (Xl.hasOwnProperty(e)) return Xl[e].call(null, this)
                        },
                        triggerElectric: Oi((function(e) {
                            Ga(this, e)
                        })),
                        findPosH: function(e, t, n, r) {
                            var i = this,
                                o = 1;
                            t < 0 && (o = -1, t = -t);
                            for (var l = Se(this.doc, e), a = 0; a < t; ++a)
                                if (l = Xa(i.doc, l, o, n, r), l.hitSide) break;
                            return l
                        },
                        moveH: Oi((function(e, t) {
                            var n = this;
                            this.extendSelectionsBy((function(r) {
                                return n.display.shift || n.doc.extend || r.empty() ? Xa(n.doc, r.head, e, t, n.options.rtlMoveVisually) : e < 0 ? r.from() : r.to()
                            }), V)
                        })),
                        deleteH: Oi((function(e, t) {
                            var n = this.doc.sel,
                                r = this.doc;
                            n.somethingSelected() ? r.replaceSelection("", null, "+delete") : Gl(this, (function(n) {
                                var i = Xa(r, n.head, e, t, !1);
                                return e < 0 ? {
                                    from: i,
                                    to: n.head
                                } : {
                                    from: n.head,
                                    to: i
                                }
                            }))
                        })),
                        findPosV: function(e, t, n, r) {
                            var i = this,
                                o = 1,
                                l = r;
                            t < 0 && (o = -1, t = -t);
                            for (var a = Se(this.doc, e), s = 0; s < t; ++s) {
                                var u = br(i, a, "div");
                                if (null == l ? l = u.left : u.left = l, a = qa(i, u, o, n), a.hitSide) break
                            }
                            return a
                        },
                        moveV: Oi((function(e, t) {
                            var n = this,
                                r = this.doc,
                                i = [],
                                o = !this.display.shift && !r.extend && r.sel.somethingSelected();
                            if (r.extendSelectionsBy((function(l) {
                                    if (o) return e < 0 ? l.from() : l.to();
                                    var a = br(n, l.head, "div");
                                    null != l.goalColumn && (a.left = l.goalColumn), i.push(a.left);
                                    var s = qa(n, a, e, t);
                                    return "page" == t && l == r.sel.primary() && ni(n, yr(n, s, "div").top - a.top), s
                                }), V), i.length)
                                for (var l = 0; l < r.sel.ranges.length; l++) r.sel.ranges[l].goalColumn = i[l]
                        })),
                        findWordAt: function(e) {
                            var t = this.doc,
                                n = ue(t, e.line).text,
                                r = e.ch,
                                i = e.ch;
                            if (n) {
                                var o = this.getHelper(e, "wordChars");
                                "before" != e.sticky && i != n.length || !r ? ++i : --r;
                                var l = n.charAt(r),
                                    a = ne(l, o) ? function(e) {
                                        return ne(e, o)
                                    } : /\s/.test(l) ? function(e) {
                                        return /\s/.test(e)
                                    } : function(e) {
                                        return !/\s/.test(e) && !ne(e)
                                    };
                                while (r > 0 && a(n.charAt(r - 1))) --r;
                                while (i < n.length && a(n.charAt(i))) ++i
                            }
                            return new ro(me(e.line, r), me(e.line, i))
                        },
                        toggleOverwrite: function(e) {
                            null != e && e == this.state.overwrite || ((this.state.overwrite = !this.state.overwrite) ? W(this.display.cursorDiv, "CodeMirror-overwrite") : T(this.display.cursorDiv, "CodeMirror-overwrite"), gt(this, "overwriteToggle", this, this.state.overwrite))
                        },
                        hasFocus: function() {
                            return this.display.input.getField() == E()
                        },
                        isReadOnly: function() {
                            return !(!this.options.readOnly && !this.doc.cantEdit)
                        },
                        scrollTo: Oi((function(e, t) {
                            ii(this, e, t)
                        })),
                        getScrollInfo: function() {
                            var e = this.display.scroller;
                            return {
                                left: e.scrollLeft,
                                top: e.scrollTop,
                                height: e.scrollHeight - Yn(this) - this.display.barHeight,
                                width: e.scrollWidth - Yn(this) - this.display.barWidth,
                                clientHeight: qn(this),
                                clientWidth: Xn(this)
                            }
                        },
                        scrollIntoView: Oi((function(e, t) {
                            null == e ? (e = {
                                from: this.doc.sel.primary().head,
                                to: null
                            }, null == t && (t = this.options.cursorScrollMargin)) : "number" == typeof e ? e = {
                                from: me(e, 0),
                                to: null
                            } : null == e.from && (e = {
                                from: e,
                                to: null
                            }), e.to || (e.to = e.from), e.margin = t || 0, null != e.from.line ? oi(this, e) : ai(this, e.from, e.to, e.margin)
                        })),
                        setSize: Oi((function(e, t) {
                            var n = this,
                                r = function(e) {
                                    return "number" == typeof e || /^\d+$/.test(String(e)) ? e + "px" : e
                                };
                            null != e && (this.display.wrapper.style.width = r(e)), null != t && (this.display.wrapper.style.height = r(t)), this.options.lineWrapping && fr(this);
                            var i = this.display.viewFrom;
                            this.doc.iter(i, this.display.viewTo, (function(e) {
                                if (e.widgets)
                                    for (var t = 0; t < e.widgets.length; t++)
                                        if (e.widgets[t].noHScroll) {
                                            Ei(n, i, "widget");
                                            break
                                        }++ i
                            })), this.curOp.forceUpdate = !0, gt(this, "refresh", this)
                        })),
                        operation: function(e) {
                            return Mi(this, e)
                        },
                        startOperation: function() {
                            return bi(this)
                        },
                        endOperation: function() {
                            return wi(this)
                        },
                        refresh: Oi((function() {
                            var e = this.display.cachedTextHeight;
                            Di(this), this.curOp.forceUpdate = !0, hr(this), ii(this, this.doc.scrollLeft, this.doc.scrollTop), Ki(this), (null == e || Math.abs(e - Or(this.display)) > .5) && Hr(this), gt(this, "refresh", this)
                        })),
                        swapDoc: Oi((function(e) {
                            var t = this.doc;
                            return t.cm = null, mo(this, e), hr(this), this.display.input.reset(), ii(this, e.scrollLeft, e.scrollTop), this.curOp.forceScroll = !0, On(this, "swapDoc", this, t), t
                        })),
                        phrase: function(e) {
                            var t = this.options.phrases;
                            return t && Object.prototype.hasOwnProperty.call(t, e) ? t[e] : e
                        },
                        getInputField: function() {
                            return this.display.input.getField()
                        },
                        getWrapperElement: function() {
                            return this.display.wrapper
                        },
                        getScrollerElement: function() {
                            return this.display.scroller
                        },
                        getGutterElement: function() {
                            return this.display.gutters
                        }
                    }, bt(e), e.registerHelper = function(t, r, i) {
                        n.hasOwnProperty(t) || (n[t] = e[t] = {
                            _global: []
                        }), n[t][r] = i
                    }, e.registerGlobalHelper = function(t, r, i, o) {
                        e.registerHelper(t, r, o), n[t]._global.push({
                            pred: i,
                            val: o
                        })
                    }
                }

                function Xa(e, t, n, r, i) {
                    var o = t,
                        l = n,
                        a = ue(e, t.line);

                    function s() {
                        var r = t.line + n;
                        return !(r < e.first || r >= e.first + e.size) && (t = new me(r, t.ch, t.sticky), a = ue(e, r))
                    }

                    function u(r) {
                        var o;
                        if (o = i ? Yl(e.cm, a, t, n) : Ul(a, t, n), null == o) {
                            if (r || !s()) return !1;
                            t = Kl(i, e.cm, a, t.line, n)
                        } else t = o;
                        return !0
                    }
                    if ("char" == r) u();
                    else if ("column" == r) u(!0);
                    else if ("word" == r || "group" == r)
                        for (var c = null, f = "group" == r, h = e.cm && e.cm.getHelper(t, "wordChars"), d = !0;; d = !1) {
                            if (n < 0 && !u(!d)) break;
                            var p = a.text.charAt(t.ch) || "\n",
                                g = ne(p, h) ? "w" : f && "\n" == p ? "n" : !f || /\s/.test(p) ? null : "p";
                            if (!f || d || g || (g = "s"), c && c != g) {
                                n < 0 && (n = 1, u(), t.sticky = "after");
                                break
                            }
                            if (g && (c = g), n > 0 && !u(!d)) break
                        }
                    var v = Uo(e, t, o, l, !0);
                    return be(o, v) && (v.hitSide = !0), v
                }

                function qa(e, t, n, r) {
                    var i, o, l = e.doc,
                        a = t.left;
                    if ("page" == r) {
                        var s = Math.min(e.display.wrapper.clientHeight, window.innerHeight || document.documentElement.clientHeight),
                            u = Math.max(s - .5 * Or(e.display), 3);
                        i = (n > 0 ? t.bottom : t.top) + n * u
                    } else "line" == r && (i = n > 0 ? t.bottom + 3 : t.top - 3);
                    for (;;) {
                        if (o = kr(e, a, i), !o.outside) break;
                        if (n < 0 ? i <= 0 : i >= l.height) {
                            o.hitSide = !0;
                            break
                        }
                        i += 5 * n
                    }
                    return o
                }
                var Ja = function(e) {
                    this.cm = e, this.lastAnchorNode = this.lastAnchorOffset = this.lastFocusNode = this.lastFocusOffset = null, this.polling = new z, this.composing = null, this.gracePeriod = !1, this.readDOMTimeout = null
                };

                function Za(e, t) {
                    var n = tr(e, t.line);
                    if (!n || n.hidden) return null;
                    var r = ue(e.doc, t.line),
                        i = Zn(n, r, t.line),
                        o = ct(r, e.doc.direction),
                        l = "left";
                    if (o) {
                        var a = st(o, t.ch);
                        l = a % 2 ? "right" : "left"
                    }
                    var s = lr(i.map, t.ch, l);
                    return s.offset = "right" == s.collapse ? s.end : s.start, s
                }

                function Qa(e) {
                    for (var t = e; t; t = t.parentNode)
                        if (/CodeMirror-gutter-wrapper/.test(t.className)) return !0;
                    return !1
                }

                function es(e, t) {
                    return t && (e.bad = !0), e
                }

                function ts(e, t, n, r, i) {
                    var o = "",
                        l = !1,
                        a = e.doc.lineSeparator(),
                        s = !1;

                    function u(e) {
                        return function(t) {
                            return t.id == e
                        }
                    }

                    function c() {
                        l && (o += a, s && (o += a), l = s = !1)
                    }

                    function f(e) {
                        e && (c(), o += e)
                    }

                    function h(t) {
                        if (1 == t.nodeType) {
                            var n = t.getAttribute("cm-text");
                            if (n) return void f(n);
                            var o, d = t.getAttribute("cm-marker");
                            if (d) {
                                var p = e.findMarks(me(r, 0), me(i + 1, 0), u(+d));
                                return void(p.length && (o = p[0].find(0)) && f(ce(e.doc, o.from, o.to).join(a)))
                            }
                            if ("false" == t.getAttribute("contenteditable")) return;
                            var g = /^(pre|div|p|li|table|br)$/i.test(t.nodeName);
                            if (!/^br$/i.test(t.nodeName) && 0 == t.textContent.length) return;
                            g && c();
                            for (var v = 0; v < t.childNodes.length; v++) h(t.childNodes[v]);
                            /^(pre|p)$/i.test(t.nodeName) && (s = !0), g && (l = !0)
                        } else 3 == t.nodeType && f(t.nodeValue.replace(/\u200b/g, "").replace(/\u00a0/g, " "))
                    }
                    for (;;) {
                        if (h(t), t == n) break;
                        t = t.nextSibling, s = !1
                    }
                    return o
                }

                function ns(e, t, n) {
                    var r;
                    if (t == e.display.lineDiv) {
                        if (r = e.display.lineDiv.childNodes[n], !r) return es(e.clipPos(me(e.display.viewTo - 1)), !0);
                        t = null, n = 0
                    } else
                        for (r = t;; r = r.parentNode) {
                            if (!r || r == e.display.lineDiv) return null;
                            if (r.parentNode && r.parentNode == e.display.lineDiv) break
                        }
                    for (var i = 0; i < e.display.view.length; i++) {
                        var o = e.display.view[i];
                        if (o.node == r) return rs(o, t, n)
                    }
                }

                function rs(e, t, n) {
                    var r = e.text.firstChild,
                        i = !1;
                    if (!t || !D(r, t)) return es(me(de(e.line), 0), !0);
                    if (t == r && (i = !0, t = r.childNodes[n], n = 0, !t)) {
                        var o = e.rest ? X(e.rest) : e.line;
                        return es(me(de(o), o.text.length), i)
                    }
                    var l = 3 == t.nodeType ? t : null,
                        a = t;
                    l || 1 != t.childNodes.length || 3 != t.firstChild.nodeType || (l = t.firstChild, n && (n = l.nodeValue.length));
                    while (a.parentNode != r) a = a.parentNode;
                    var s = e.measure,
                        u = s.maps;

                    function c(t, n, r) {
                        for (var i = -1; i < (u ? u.length : 0); i++)
                            for (var o = i < 0 ? s.map : u[i], l = 0; l < o.length; l += 3) {
                                var a = o[l + 2];
                                if (a == t || a == n) {
                                    var c = de(i < 0 ? e.line : e.rest[i]),
                                        f = o[l] + r;
                                    return (r < 0 || a != t) && (f = o[l + (r ? 1 : 0)]), me(c, f)
                                }
                            }
                    }
                    var f = c(l, a, n);
                    if (f) return es(f, i);
                    for (var h = a.nextSibling, d = l ? l.nodeValue.length - n : 0; h; h = h.nextSibling) {
                        if (f = c(h, h.firstChild, 0), f) return es(me(f.line, f.ch - d), i);
                        d += h.textContent.length
                    }
                    for (var p = a.previousSibling, g = n; p; p = p.previousSibling) {
                        if (f = c(p, p.firstChild, -1), f) return es(me(f.line, f.ch + g), i);
                        g += p.textContent.length
                    }
                }
                Ja.prototype.init = function(e) {
                    var t = this,
                        n = this,
                        r = n.cm,
                        i = n.div = e.lineDiv;

                    function o(e) {
                        if (!vt(r, e)) {
                            if (r.somethingSelected()) $a({
                                lineWise: !1,
                                text: r.getSelections()
                            }), "cut" == e.type && r.replaceSelection("", null, "cut");
                            else {
                                if (!r.options.lineWiseCopyCut) return;
                                var t = Va(r);
                                $a({
                                    lineWise: !0,
                                    text: t.text
                                }), "cut" == e.type && r.operation((function() {
                                    r.setSelections(t.ranges, 0, j), r.replaceSelection("", null, "cut")
                                }))
                            }
                            if (e.clipboardData) {
                                e.clipboardData.clearData();
                                var o = Ba.text.join("\n");
                                if (e.clipboardData.setData("Text", o), e.clipboardData.getData("Text") == o) return void e.preventDefault()
                            }
                            var l = Ka(),
                                a = l.firstChild;
                            r.display.lineSpace.insertBefore(l, r.display.lineSpace.firstChild), a.value = Ba.text.join("\n");
                            var s = document.activeElement;
                            F(a), setTimeout((function() {
                                r.display.lineSpace.removeChild(l), s.focus(), s == i && n.showPrimarySelection()
                            }), 50)
                        }
                    }
                    Ua(i, r.options.spellcheck, r.options.autocorrect, r.options.autocapitalize), ht(i, "paste", (function(e) {
                        vt(r, e) || ja(e, r) || a <= 11 && setTimeout(Ni(r, (function() {
                            return t.updateFromDOM()
                        })), 20)
                    })), ht(i, "compositionstart", (function(e) {
                        t.composing = {
                            data: e.data,
                            done: !1
                        }
                    })), ht(i, "compositionupdate", (function(e) {
                        t.composing || (t.composing = {
                            data: e.data,
                            done: !1
                        })
                    })), ht(i, "compositionend", (function(e) {
                        t.composing && (e.data != t.composing.data && t.readFromDOMSoon(), t.composing.done = !0)
                    })), ht(i, "touchstart", (function() {
                        return n.forceCompositionEnd()
                    })), ht(i, "input", (function() {
                        t.composing || t.readFromDOMSoon()
                    })), ht(i, "copy", o), ht(i, "cut", o)
                }, Ja.prototype.prepareSelection = function() {
                    var e = Rr(this.cm, !1);
                    return e.focus = this.cm.state.focused, e
                }, Ja.prototype.showSelection = function(e, t) {
                    e && this.cm.display.view.length && ((e.focus || t) && this.showPrimarySelection(), this.showMultipleSelections(e))
                }, Ja.prototype.getSelection = function() {
                    return this.cm.display.wrapper.ownerDocument.getSelection()
                }, Ja.prototype.showPrimarySelection = function() {
                    var e = this.getSelection(),
                        t = this.cm,
                        r = t.doc.sel.primary(),
                        i = r.from(),
                        o = r.to();
                    if (t.display.viewTo == t.display.viewFrom || i.line >= t.display.viewTo || o.line < t.display.viewFrom) e.removeAllRanges();
                    else {
                        var l = ns(t, e.anchorNode, e.anchorOffset),
                            a = ns(t, e.focusNode, e.focusOffset);
                        if (!l || l.bad || !a || a.bad || 0 != ye(ke(l, a), i) || 0 != ye(xe(l, a), o)) {
                            var s = t.display.view,
                                u = i.line >= t.display.viewFrom && Za(t, i) || {
                                    node: s[0].measure.map[2],
                                    offset: 0
                                },
                                c = o.line < t.display.viewTo && Za(t, o);
                            if (!c) {
                                var f = s[s.length - 1].measure,
                                    h = f.maps ? f.maps[f.maps.length - 1] : f.map;
                                c = {
                                    node: h[h.length - 1],
                                    offset: h[h.length - 2] - h[h.length - 3]
                                }
                            }
                            if (u && c) {
                                var d, p = e.rangeCount && e.getRangeAt(0);
                                try {
                                    d = L(u.node, u.offset, c.offset, c.node)
                                } catch (g) {}
                                d && (!n && t.state.focused ? (e.collapse(u.node, u.offset), d.collapsed || (e.removeAllRanges(), e.addRange(d))) : (e.removeAllRanges(), e.addRange(d)), p && null == e.anchorNode ? e.addRange(p) : n && this.startGracePeriod()), this.rememberSelection()
                            } else e.removeAllRanges()
                        }
                    }
                }, Ja.prototype.startGracePeriod = function() {
                    var e = this;
                    clearTimeout(this.gracePeriod), this.gracePeriod = setTimeout((function() {
                        e.gracePeriod = !1, e.selectionChanged() && e.cm.operation((function() {
                            return e.cm.curOp.selectionChanged = !0
                        }))
                    }), 20)
                }, Ja.prototype.showMultipleSelections = function(e) {
                    N(this.cm.display.cursorDiv, e.cursors), N(this.cm.display.selectionDiv, e.selection)
                }, Ja.prototype.rememberSelection = function() {
                    var e = this.getSelection();
                    this.lastAnchorNode = e.anchorNode, this.lastAnchorOffset = e.anchorOffset, this.lastFocusNode = e.focusNode, this.lastFocusOffset = e.focusOffset
                }, Ja.prototype.selectionInEditor = function() {
                    var e = this.getSelection();
                    if (!e.rangeCount) return !1;
                    var t = e.getRangeAt(0).commonAncestorContainer;
                    return D(this.div, t)
                }, Ja.prototype.focus = function() {
                    "nocursor" != this.cm.options.readOnly && (this.selectionInEditor() || this.showSelection(this.prepareSelection(), !0), this.div.focus())
                }, Ja.prototype.blur = function() {
                    this.div.blur()
                }, Ja.prototype.getField = function() {
                    return this.div
                }, Ja.prototype.supportsTouch = function() {
                    return !0
                }, Ja.prototype.receivedFocus = function() {
                    var e = this;

                    function t() {
                        e.cm.state.focused && (e.pollSelection(), e.polling.set(e.cm.options.pollInterval, t))
                    }
                    this.selectionInEditor() ? this.pollSelection() : Mi(this.cm, (function() {
                        return e.cm.curOp.selectionChanged = !0
                    })), this.polling.set(this.cm.options.pollInterval, t)
                }, Ja.prototype.selectionChanged = function() {
                    var e = this.getSelection();
                    return e.anchorNode != this.lastAnchorNode || e.anchorOffset != this.lastAnchorOffset || e.focusNode != this.lastFocusNode || e.focusOffset != this.lastFocusOffset
                }, Ja.prototype.pollSelection = function() {
                    if (null == this.readDOMTimeout && !this.gracePeriod && this.selectionChanged()) {
                        var e = this.getSelection(),
                            t = this.cm;
                        if (v && c && this.cm.options.gutters.length && Qa(e.anchorNode)) return this.cm.triggerOnKeyDown({
                            type: "keydown",
                            keyCode: 8,
                            preventDefault: Math.abs
                        }), this.blur(), void this.focus();
                        if (!this.composing) {
                            this.rememberSelection();
                            var n = ns(t, e.anchorNode, e.anchorOffset),
                                r = ns(t, e.focusNode, e.focusOffset);
                            n && r && Mi(t, (function() {
                                Bo(t.doc, oo(n, r), j), (n.bad || r.bad) && (t.curOp.selectionChanged = !0)
                            }))
                        }
                    }
                }, Ja.prototype.pollContent = function() {
                    null != this.readDOMTimeout && (clearTimeout(this.readDOMTimeout), this.readDOMTimeout = null);
                    var e, t, n, r = this.cm,
                        i = r.display,
                        o = r.doc.sel.primary(),
                        l = o.from(),
                        a = o.to();
                    if (0 == l.ch && l.line > r.firstLine() && (l = me(l.line - 1, ue(r.doc, l.line - 1).length)), a.ch == ue(r.doc, a.line).text.length && a.line < r.lastLine() && (a = me(a.line + 1, 0)), l.line < i.viewFrom || a.line > i.viewTo - 1) return !1;
                    l.line == i.viewFrom || 0 == (e = Ir(r, l.line)) ? (t = de(i.view[0].line), n = i.view[0].node) : (t = de(i.view[e].line), n = i.view[e - 1].node.nextSibling);
                    var s, u, c = Ir(r, a.line);
                    if (c == i.view.length - 1 ? (s = i.viewTo - 1, u = i.lineDiv.lastChild) : (s = de(i.view[c + 1].line) - 1, u = i.view[c + 1].node.previousSibling), !n) return !1;
                    var f = r.doc.splitLines(ts(r, n, u, t, s)),
                        h = ce(r.doc, me(t, 0), me(s, ue(r.doc, s).text.length));
                    while (f.length > 1 && h.length > 1)
                        if (X(f) == X(h)) f.pop(), h.pop(), s--;
                        else {
                            if (f[0] != h[0]) break;
                            f.shift(), h.shift(), t++
                        } var d = 0,
                        p = 0,
                        g = f[0],
                        v = h[0],
                        m = Math.min(g.length, v.length);
                    while (d < m && g.charCodeAt(d) == v.charCodeAt(d)) ++d;
                    var y = X(f),
                        b = X(h),
                        w = Math.min(y.length - (1 == f.length ? d : 0), b.length - (1 == h.length ? d : 0));
                    while (p < w && y.charCodeAt(y.length - p - 1) == b.charCodeAt(b.length - p - 1)) ++p;
                    if (1 == f.length && 1 == h.length && t == l.line)
                        while (d && d > l.ch && y.charCodeAt(y.length - p - 1) == b.charCodeAt(b.length - p - 1)) d--, p++;
                    f[f.length - 1] = y.slice(0, y.length - p).replace(/^\u200b+/, ""), f[0] = f[0].slice(d).replace(/\u200b+$/, "");
                    var x = me(t, d),
                        k = me(s, h.length ? X(h).length - p : 0);
                    return f.length > 1 || f[0] || ye(x, k) ? (nl(r.doc, f, x, k, "+input"), !0) : void 0
                }, Ja.prototype.ensurePolled = function() {
                    this.forceCompositionEnd()
                }, Ja.prototype.reset = function() {
                    this.forceCompositionEnd()
                }, Ja.prototype.forceCompositionEnd = function() {
                    this.composing && (clearTimeout(this.readDOMTimeout), this.composing = null, this.updateFromDOM(), this.div.blur(), this.div.focus())
                }, Ja.prototype.readFromDOMSoon = function() {
                    var e = this;
                    null == this.readDOMTimeout && (this.readDOMTimeout = setTimeout((function() {
                        if (e.readDOMTimeout = null, e.composing) {
                            if (!e.composing.done) return;
                            e.composing = null
                        }
                        e.updateFromDOM()
                    }), 80))
                }, Ja.prototype.updateFromDOM = function() {
                    var e = this;
                    !this.cm.isReadOnly() && this.pollContent() || Mi(this.cm, (function() {
                        return Di(e.cm)
                    }))
                }, Ja.prototype.setUneditable = function(e) {
                    e.contentEditable = "false"
                }, Ja.prototype.onKeyPress = function(e) {
                    0 == e.charCode || this.composing || (e.preventDefault(), this.cm.isReadOnly() || Ni(this.cm, _a)(this.cm, String.fromCharCode(null == e.charCode ? e.keyCode : e.charCode), 0))
                }, Ja.prototype.readOnlyChanged = function(e) {
                    this.div.contentEditable = String("nocursor" != e)
                }, Ja.prototype.onContextMenu = function() {}, Ja.prototype.resetPosition = function() {}, Ja.prototype.needsContentAttribute = !0;
                var is = function(e) {
                    this.cm = e, this.prevInput = "", this.pollingFast = !1, this.polling = new z, this.hasSelection = !1, this.composing = null
                };

                function os(e, t) {
                    if (t = t ? P(t) : {}, t.value = e.value, !t.tabindex && e.tabIndex && (t.tabindex = e.tabIndex), !t.placeholder && e.placeholder && (t.placeholder = e.placeholder), null == t.autofocus) {
                        var n = E();
                        t.autofocus = n == e || null != e.getAttribute("autofocus") && n == document.body
                    }

                    function r() {
                        e.value = a.getValue()
                    }
                    var i;
                    if (e.form && (ht(e.form, "submit", r), !t.leaveSubmitMethodAlone)) {
                        var o = e.form;
                        i = o.submit;
                        try {
                            var l = o.submit = function() {
                                r(), o.submit = i, o.submit(), o.submit = l
                            }
                        } catch (s) {}
                    }
                    t.finishInit = function(t) {
                        t.save = r, t.getTextArea = function() {
                            return e
                        }, t.toTextArea = function() {
                            t.toTextArea = isNaN, r(), e.parentNode.removeChild(t.getWrapperElement()), e.style.display = "", e.form && (pt(e.form, "submit", r), "function" == typeof e.form.submit && (e.form.submit = i))
                        }
                    }, e.style.display = "none";
                    var a = Ia((function(t) {
                        return e.parentNode.insertBefore(t, e.nextSibling)
                    }), t);
                    return a
                }

                function ls(e) {
                    e.off = pt, e.on = ht, e.wheelEventPixels = eo, e.Doc = xl, e.splitLines = Dt, e.countColumn = R, e.findColumn = U, e.isWordChar = te, e.Pass = _, e.signal = gt, e.Line = un, e.changeEnd = lo, e.scrollbarModel = vi, e.Pos = me, e.cmpPos = ye, e.modes = It, e.mimeModes = Pt, e.resolveMode = Bt, e.getMode = $t, e.modeExtensions = _t, e.extendMode = jt, e.copyState = Gt, e.startState = Ut, e.innerMode = Vt, e.commands = Xl, e.keyMap = Il, e.keyName = _l, e.isModifierKey = Bl, e.lookupKey = zl, e.normalizeKeyMap = Rl, e.StringStream = Kt, e.SharedTextMarker = gl, e.TextMarker = dl, e.LineWidget = ul, e.e_preventDefault = wt, e.e_stopPropagation = xt, e.e_stop = Ct, e.addClass = W, e.contains = D, e.rmClass = T, e.keyNames = El
                }
                is.prototype.init = function(e) {
                    var t = this,
                        n = this,
                        r = this.cm;
                    this.createField(e);
                    var i = this.textarea;

                    function o(e) {
                        if (!vt(r, e)) {
                            if (r.somethingSelected()) $a({
                                lineWise: !1,
                                text: r.getSelections()
                            });
                            else {
                                if (!r.options.lineWiseCopyCut) return;
                                var t = Va(r);
                                $a({
                                    lineWise: !0,
                                    text: t.text
                                }), "cut" == e.type ? r.setSelections(t.ranges, null, j) : (n.prevInput = "", i.value = t.text.join("\n"), F(i))
                            }
                            "cut" == e.type && (r.state.cutIncoming = +new Date)
                        }
                    }
                    e.wrapper.insertBefore(this.wrapper, e.wrapper.firstChild), g && (i.style.width = "0px"), ht(i, "input", (function() {
                        l && a >= 9 && t.hasSelection && (t.hasSelection = null), n.poll()
                    })), ht(i, "paste", (function(e) {
                        vt(r, e) || ja(e, r) || (r.state.pasteIncoming = +new Date, n.fastPoll())
                    })), ht(i, "cut", o), ht(i, "copy", o), ht(e.scroller, "paste", (function(t) {
                        if (!Gn(e, t) && !vt(r, t)) {
                            if (!i.dispatchEvent) return r.state.pasteIncoming = +new Date, void n.focus();
                            var o = new Event("paste");
                            o.clipboardData = t.clipboardData, i.dispatchEvent(o)
                        }
                    })), ht(e.lineSpace, "selectstart", (function(t) {
                        Gn(e, t) || wt(t)
                    })), ht(i, "compositionstart", (function() {
                        var e = r.getCursor("from");
                        n.composing && n.composing.range.clear(), n.composing = {
                            start: e,
                            range: r.markText(e, r.getCursor("to"), {
                                className: "CodeMirror-composing"
                            })
                        }
                    })), ht(i, "compositionend", (function() {
                        n.composing && (n.poll(), n.composing.range.clear(), n.composing = null)
                    }))
                }, is.prototype.createField = function(e) {
                    this.wrapper = Ka(), this.textarea = this.wrapper.firstChild
                }, is.prototype.prepareSelection = function() {
                    var e = this.cm,
                        t = e.display,
                        n = e.doc,
                        r = Rr(e);
                    if (e.options.moveInputWithCursor) {
                        var i = br(e, n.sel.primary().head, "div"),
                            o = t.wrapper.getBoundingClientRect(),
                            l = t.lineDiv.getBoundingClientRect();
                        r.teTop = Math.max(0, Math.min(t.wrapper.clientHeight - 10, i.top + l.top - o.top)), r.teLeft = Math.max(0, Math.min(t.wrapper.clientWidth - 10, i.left + l.left - o.left))
                    }
                    return r
                }, is.prototype.showSelection = function(e) {
                    var t = this.cm,
                        n = t.display;
                    N(n.cursorDiv, e.cursors), N(n.selectionDiv, e.selection), null != e.teTop && (this.wrapper.style.top = e.teTop + "px", this.wrapper.style.left = e.teLeft + "px")
                }, is.prototype.reset = function(e) {
                    if (!this.contextMenuPending && !this.composing) {
                        var t = this.cm;
                        if (t.somethingSelected()) {
                            this.prevInput = "";
                            var n = t.getSelection();
                            this.textarea.value = n, t.state.focused && F(this.textarea), l && a >= 9 && (this.hasSelection = n)
                        } else e || (this.prevInput = this.textarea.value = "", l && a >= 9 && (this.hasSelection = null))
                    }
                }, is.prototype.getField = function() {
                    return this.textarea
                }, is.prototype.supportsTouch = function() {
                    return !1
                }, is.prototype.focus = function() {
                    if ("nocursor" != this.cm.options.readOnly && (!m || E() != this.textarea)) try {
                        this.textarea.focus()
                    } catch (e) {}
                }, is.prototype.blur = function() {
                    this.textarea.blur()
                }, is.prototype.resetPosition = function() {
                    this.wrapper.style.top = this.wrapper.style.left = 0
                }, is.prototype.receivedFocus = function() {
                    this.slowPoll()
                }, is.prototype.slowPoll = function() {
                    var e = this;
                    this.pollingFast || this.polling.set(this.cm.options.pollInterval, (function() {
                        e.poll(), e.cm.state.focused && e.slowPoll()
                    }))
                }, is.prototype.fastPoll = function() {
                    var e = !1,
                        t = this;

                    function n() {
                        var r = t.poll();
                        r || e ? (t.pollingFast = !1, t.slowPoll()) : (e = !0, t.polling.set(60, n))
                    }
                    t.pollingFast = !0, t.polling.set(20, n)
                }, is.prototype.poll = function() {
                    var e = this,
                        t = this.cm,
                        n = this.textarea,
                        r = this.prevInput;
                    if (this.contextMenuPending || !t.state.focused || Et(n) && !r && !this.composing || t.isReadOnly() || t.options.disableInput || t.state.keySeq) return !1;
                    var i = n.value;
                    if (i == r && !t.somethingSelected()) return !1;
                    if (l && a >= 9 && this.hasSelection === i || y && /[\uf700-\uf7ff]/.test(i)) return t.display.input.reset(), !1;
                    if (t.doc.sel == t.display.selForContextMenu) {
                        var o = i.charCodeAt(0);
                        if (8203 != o || r || (r = "​"), 8666 == o) return this.reset(), this.cm.execCommand("undo")
                    }
                    var s = 0,
                        u = Math.min(r.length, i.length);
                    while (s < u && r.charCodeAt(s) == i.charCodeAt(s)) ++s;
                    return Mi(t, (function() {
                        _a(t, i.slice(s), r.length - s, null, e.composing ? "*compose" : null), i.length > 1e3 || i.indexOf("\n") > -1 ? n.value = e.prevInput = "" : e.prevInput = i, e.composing && (e.composing.range.clear(), e.composing.range = t.markText(e.composing.start, t.getCursor("to"), {
                            className: "CodeMirror-composing"
                        }))
                    })), !0
                }, is.prototype.ensurePolled = function() {
                    this.pollingFast && this.poll() && (this.pollingFast = !1)
                }, is.prototype.onKeyPress = function() {
                    l && a >= 9 && (this.hasSelection = null), this.fastPoll()
                }, is.prototype.onContextMenu = function(e) {
                    var t = this,
                        n = t.cm,
                        r = n.display,
                        i = t.textarea;
                    t.contextMenuPending && t.contextMenuPending();
                    var o = Fr(n, e),
                        u = r.scroller.scrollTop;
                    if (o && !f) {
                        var c = n.options.resetSelectionOnContextMenu;
                        c && -1 == n.doc.sel.contains(o) && Ni(n, Bo)(n.doc, oo(o), j);
                        var h, d = i.style.cssText,
                            p = t.wrapper.style.cssText,
                            g = t.wrapper.offsetParent.getBoundingClientRect();
                        if (t.wrapper.style.cssText = "position: static", i.style.cssText = "position: absolute; width: 30px; height: 30px;\n      top: " + (e.clientY - g.top - 5) + "px; left: " + (e.clientX - g.left - 5) + "px;\n      z-index: 1000; background: " + (l ? "rgba(255, 255, 255, .05)" : "transparent") + ";\n      outline: none; border-width: 0; outline: none; overflow: hidden; opacity: .05; filter: alpha(opacity=5);", s && (h = window.scrollY), r.input.focus(), s && window.scrollTo(null, h), r.input.reset(), n.somethingSelected() || (i.value = t.prevInput = " "), t.contextMenuPending = y, r.selForContextMenu = n.doc.sel, clearTimeout(r.detectingSelectAll), l && a >= 9 && m(), C) {
                            Ct(e);
                            var v = function() {
                                pt(window, "mouseup", v), setTimeout(y, 20)
                            };
                            ht(window, "mouseup", v)
                        } else setTimeout(y, 50)
                    }

                    function m() {
                        if (null != i.selectionStart) {
                            var e = n.somethingSelected(),
                                o = "​" + (e ? i.value : "");
                            i.value = "⇚", i.value = o, t.prevInput = e ? "" : "​", i.selectionStart = 1, i.selectionEnd = o.length, r.selForContextMenu = n.doc.sel
                        }
                    }

                    function y() {
                        if (t.contextMenuPending == y && (t.contextMenuPending = !1, t.wrapper.style.cssText = p, i.style.cssText = d, l && a < 9 && r.scrollbars.setScrollTop(r.scroller.scrollTop = u), null != i.selectionStart)) {
                            (!l || l && a < 9) && m();
                            var e = 0,
                                o = function() {
                                    r.selForContextMenu == n.doc.sel && 0 == i.selectionStart && i.selectionEnd > 0 && "​" == t.prevInput ? Ni(n, Yo)(n) : e++ < 10 ? r.detectingSelectAll = setTimeout(o, 500) : (r.selForContextMenu = null, r.input.reset())
                                };
                            r.detectingSelectAll = setTimeout(o, 200)
                        }
                    }
                }, is.prototype.readOnlyChanged = function(e) {
                    e || this.reset(), this.textarea.disabled = "nocursor" == e
                }, is.prototype.setUneditable = function() {}, is.prototype.needsContentAttribute = !1, Ea(Ia), Ya(Ia);
                var as = "iter insert remove copy getEditor constructor".split(" ");
                for (var ss in xl.prototype) xl.prototype.hasOwnProperty(ss) && B(as, ss) < 0 && (Ia.prototype[ss] = function(e) {
                    return function() {
                        return e.apply(this.doc, arguments)
                    }
                }(xl.prototype[ss]));
                return bt(xl), Ia.inputStyles = {
                    textarea: is,
                    contenteditable: Ja
                }, Ia.defineMode = function(e) {
                    Ia.defaults.mode || "null" == e || (Ia.defaults.mode = e), Rt.apply(this, arguments)
                }, Ia.defineMIME = zt, Ia.defineMode("null", (function() {
                    return {
                        token: function(e) {
                            return e.skipToEnd()
                        }
                    }
                })), Ia.defineMIME("text/plain", "null"), Ia.defineExtension = function(e, t) {
                    Ia.prototype[e] = t
                }, Ia.defineDocExtension = function(e, t) {
                    xl.prototype[e] = t
                }, Ia.fromTextArea = os, ls(Ia), Ia.version = "5.45.0", Ia
            }))
        },
        8822: function(e, t, n) {
            (function(e) {
                e(n("56b3"))
            })((function(e) {
                "use strict";
                var t = "CodeMirror-lint-markers";

                function n(t, n) {
                    var r = document.createElement("div");

                    function i(t) {
                        if (!r.parentNode) return e.off(document, "mousemove", i);
                        r.style.top = Math.max(0, t.clientY - r.offsetHeight - 5) + "px", r.style.left = t.clientX + 5 + "px"
                    }
                    return r.className = "CodeMirror-lint-tooltip", r.appendChild(n.cloneNode(!0)), document.body.appendChild(r), e.on(document, "mousemove", i), i(t), null != r.style.opacity && (r.style.opacity = 1), r
                }

                function r(e) {
                    e.parentNode && e.parentNode.removeChild(e)
                }

                function i(e) {
                    e.parentNode && (null == e.style.opacity && r(e), e.style.opacity = 0, setTimeout((function() {
                        r(e)
                    }), 600))
                }

                function o(t, r, o) {
                    var l = n(t, r);

                    function a() {
                        e.off(o, "mouseout", a), l && (i(l), l = null)
                    }
                    var s = setInterval((function() {
                        if (l)
                            for (var e = o;; e = e.parentNode) {
                                if (e && 11 == e.nodeType && (e = e.host), e == document.body) return;
                                if (!e) {
                                    a();
                                    break
                                }
                            }
                        if (!l) return clearInterval(s)
                    }), 400);
                    e.on(o, "mouseout", a)
                }

                function l(e, t, n) {
                    this.marked = [], this.options = t, this.timeout = null, this.hasGutter = n, this.onMouseOver = function(t) {
                        y(e, t)
                    }, this.waitingFor = 0
                }

                function a(e, t) {
                    return t instanceof Function ? {
                        getAnnotations: t
                    } : (t && !0 !== t || (t = {}), t)
                }

                function s(e) {
                    var n = e.state.lint;
                    n.hasGutter && e.clearGutter(t);
                    for (var r = 0; r < n.marked.length; ++r) n.marked[r].clear();
                    n.marked.length = 0
                }

                function u(t, n, r, i) {
                    var l = document.createElement("div"),
                        a = l;
                    return l.className = "CodeMirror-lint-marker-" + n, r && (a = l.appendChild(document.createElement("div")), a.className = "CodeMirror-lint-marker-multiple"), 0 != i && e.on(a, "mouseover", (function(e) {
                        o(e, t, a)
                    })), l
                }

                function c(e, t) {
                    return "error" == e ? e : t
                }

                function f(e) {
                    for (var t = [], n = 0; n < e.length; ++n) {
                        var r = e[n],
                            i = r.from.line;
                        (t[i] || (t[i] = [])).push(r)
                    }
                    return t
                }

                function h(e) {
                    var t = e.severity;
                    t || (t = "error");
                    var n = document.createElement("div");
                    return n.className = "CodeMirror-lint-message-" + t, "undefined" != typeof e.messageHTML ? n.innerHTML = e.messageHTML : n.appendChild(document.createTextNode(e.message)), n
                }

                function d(t, n, r) {
                    var i = t.state.lint,
                        o = ++i.waitingFor;

                    function l() {
                        o = -1, t.off("change", l)
                    }
                    t.on("change", l), n(t.getValue(), (function(n, r) {
                        t.off("change", l), i.waitingFor == o && (r && n instanceof e && (n = r), t.operation((function() {
                            g(t, n)
                        })))
                    }), r, t)
                }

                function p(t) {
                    var n = t.state.lint,
                        r = n.options,
                        i = r.options || r,
                        o = r.getAnnotations || t.getHelper(e.Pos(0, 0), "lint");
                    if (o)
                        if (r.async || o.async) d(t, o, i);
                        else {
                            var l = o(t.getValue(), i, t);
                            if (!l) return;
                            l.then ? l.then((function(e) {
                                t.operation((function() {
                                    g(t, e)
                                }))
                            })) : t.operation((function() {
                                g(t, l)
                            }))
                        }
                }

                function g(e, n) {
                    s(e);
                    for (var r = e.state.lint, i = r.options, o = f(n), l = 0; l < o.length; ++l) {
                        var a = o[l];
                        if (a) {
                            for (var d = null, p = r.hasGutter && document.createDocumentFragment(), g = 0; g < a.length; ++g) {
                                var v = a[g],
                                    m = v.severity;
                                m || (m = "error"), d = c(d, m), i.formatAnnotation && (v = i.formatAnnotation(v)), r.hasGutter && p.appendChild(h(v)), v.to && r.marked.push(e.markText(v.from, v.to, {
                                    className: "CodeMirror-lint-mark-" + m,
                                    __annotation: v
                                }))
                            }
                            r.hasGutter && e.setGutterMarker(l, t, u(p, d, a.length > 1, r.options.tooltips))
                        }
                    }
                    i.onUpdateLinting && i.onUpdateLinting(n, o, e)
                }

                function v(e) {
                    var t = e.state.lint;
                    t && (clearTimeout(t.timeout), t.timeout = setTimeout((function() {
                        p(e)
                    }), t.options.delay || 500))
                }

                function m(e, t) {
                    for (var n = t.target || t.srcElement, r = document.createDocumentFragment(), i = 0; i < e.length; i++) {
                        var l = e[i];
                        r.appendChild(h(l))
                    }
                    o(t, r, n)
                }

                function y(e, t) {
                    var n = t.target || t.srcElement;
                    if (/\bCodeMirror-lint-mark-/.test(n.className)) {
                        for (var r = n.getBoundingClientRect(), i = (r.left + r.right) / 2, o = (r.top + r.bottom) / 2, l = e.findMarksAt(e.coordsChar({
                                left: i,
                                top: o
                            }, "client")), a = [], s = 0; s < l.length; ++s) {
                            var u = l[s].__annotation;
                            u && a.push(u)
                        }
                        a.length && m(a, t)
                    }
                }
                e.defineOption("lint", !1, (function(n, r, i) {
                    if (i && i != e.Init && (s(n), !1 !== n.state.lint.options.lintOnChange && n.off("change", v), e.off(n.getWrapperElement(), "mouseover", n.state.lint.onMouseOver), clearTimeout(n.state.lint.timeout), delete n.state.lint), r) {
                        for (var o = n.getOption("gutters"), u = !1, c = 0; c < o.length; ++c) o[c] == t && (u = !0);
                        var f = n.state.lint = new l(n, a(n, r), u);
                        !1 !== f.options.lintOnChange && n.on("change", v), 0 != f.options.tooltips && "gutter" != f.options.tooltips && e.on(n.getWrapperElement(), "mouseover", f.onMouseOver), p(n)
                    }
                })), e.defineExtension("performLint", (function() {
                    this.state.lint && p(this)
                }))
            }))
        },
        a7be: function(e, t, n) {},
        acdf: function(e, t, n) {},
        ae67: function(e, t, n) {
            n("f2b5")(n("3f23"))
        },
        d2de: function(e, t, n) {
            (function(e) {
                e(n("56b3"))
            })((function(e) {
                "use strict";
                e.registerHelper("lint", "json", (function(t) {
                    var n = [];
                    if (!window.jsonlint) return window.console && window.console.error("Error: window.jsonlint not defined, CodeMirror JSON linting cannot run."), n;
                    var r = window.jsonlint.parser || window.jsonlint;
                    r.parseError = function(t, r) {
                        var i = r.loc;
                        n.push({
                            from: e.Pos(i.first_line - 1, i.first_column),
                            to: e.Pos(i.last_line - 1, i.last_column),
                            message: t
                        })
                    };
                    try {
                        r.parse(t)
                    } catch (i) {}
                    return n
                }))
            }))
        },
        f2b5: function(e, t) {
            e.exports = function(e) {
                function t(e) {
                    "undefined" !== typeof console && (console.error || console.log)("[Script Loader]", e)
                }

                function n() {
                    return "undefined" !== typeof attachEvent && "undefined" === typeof addEventListener
                }
                try {
                    "undefined" !== typeof execScript && n() ? execScript(e) : "undefined" !== typeof eval ? eval.call(null, e) : t("EvalError: No eval function available")
                } catch (r) {
                    t(r)
                }
            }
        },
        f9d4: function(e, t, n) {
            (function(e) {
                e(n("56b3"))
            })((function(e) {
                "use strict";
                e.defineMode("javascript", (function(t, n) {
                    var r, i, o = t.indentUnit,
                        l = n.statementIndent,
                        a = n.jsonld,
                        s = n.json || a,
                        u = n.typescript,
                        c = n.wordCharacters || /[\w$\xa1-\uffff]/,
                        f = function() {
                            function e(e) {
                                return {
                                    type: e,
                                    style: "keyword"
                                }
                            }
                            var t = e("keyword a"),
                                n = e("keyword b"),
                                r = e("keyword c"),
                                i = e("keyword d"),
                                o = e("operator"),
                                l = {
                                    type: "atom",
                                    style: "atom"
                                };
                            return {
                                if: e("if"),
                                while: t,
                                with: t,
                                else: n,
                                do: n,
                                try: n,
                                finally: n,
                                return: i,
                                break: i,
                                continue: i,
                                new: e("new"),
                                delete: r,
                                void: r,
                                throw: r,
                                debugger: e("debugger"),
                                var: e("var"),
                                const: e("var"),
                                let: e("var"),
                                function: e("function"),
                                catch: e("catch"),
                                for: e("for"),
                                switch: e("switch"),
                                case: e("case"),
                                default: e("default"),
                                in: o,
                                typeof: o,
                                instanceof: o,
                                true: l,
                                false: l,
                                null: l,
                                undefined: l,
                                NaN: l,
                                Infinity: l,
                                this: e("this"),
                                class: e("class"),
                                super: e("atom"),
                                yield: r,
                                export: e("export"),
                                import: e("import"),
                                extends: r,
                                await: r
                            }
                        }(),
                        h = /[+\-*&%=<>!?|~^@]/,
                        d = /^@(context|id|value|language|type|container|list|set|reverse|index|base|vocab|graph)"/;

                    function p(e) {
                        var t, n = !1,
                            r = !1;
                        while (null != (t = e.next())) {
                            if (!n) {
                                if ("/" == t && !r) return;
                                "[" == t ? r = !0 : r && "]" == t && (r = !1)
                            }
                            n = !n && "\\" == t
                        }
                    }

                    function g(e, t, n) {
                        return r = e, i = n, t
                    }

                    function v(e, t) {
                        var n = e.next();
                        if ('"' == n || "'" == n) return t.tokenize = m(n), t.tokenize(e, t);
                        if ("." == n && e.match(/^\d+(?:[eE][+\-]?\d+)?/)) return g("number", "number");
                        if ("." == n && e.match("..")) return g("spread", "meta");
                        if (/[\[\]{}\(\),;\:\.]/.test(n)) return g(n);
                        if ("=" == n && e.eat(">")) return g("=>", "operator");
                        if ("0" == n && e.match(/^(?:x[\da-f]+|o[0-7]+|b[01]+)n?/i)) return g("number", "number");
                        if (/\d/.test(n)) return e.match(/^\d*(?:n|(?:\.\d*)?(?:[eE][+\-]?\d+)?)?/), g("number", "number");
                        if ("/" == n) return e.eat("*") ? (t.tokenize = y, y(e, t)) : e.eat("/") ? (e.skipToEnd(), g("comment", "comment")) : Qe(e, t, 1) ? (p(e), e.match(/^\b(([gimyus])(?![gimyus]*\2))+\b/), g("regexp", "string-2")) : (e.eat("="), g("operator", "operator", e.current()));
                        if ("`" == n) return t.tokenize = b, b(e, t);
                        if ("#" == n) return e.skipToEnd(), g("error", "error");
                        if (h.test(n)) return ">" == n && t.lexical && ">" == t.lexical.type || (e.eat("=") ? "!" != n && "=" != n || e.eat("=") : /[<>*+\-]/.test(n) && (e.eat(n), ">" == n && e.eat(n))), g("operator", "operator", e.current());
                        if (c.test(n)) {
                            e.eatWhile(c);
                            var r = e.current();
                            if ("." != t.lastType) {
                                if (f.propertyIsEnumerable(r)) {
                                    var i = f[r];
                                    return g(i.type, i.style, r)
                                }
                                if ("async" == r && e.match(/^(\s|\/\*.*?\*\/)*[\[\(\w]/, !1)) return g("async", "keyword", r)
                            }
                            return g("variable", "variable", r)
                        }
                    }

                    function m(e) {
                        return function(t, n) {
                            var r, i = !1;
                            if (a && "@" == t.peek() && t.match(d)) return n.tokenize = v, g("jsonld-keyword", "meta");
                            while (null != (r = t.next())) {
                                if (r == e && !i) break;
                                i = !i && "\\" == r
                            }
                            return i || (n.tokenize = v), g("string", "string")
                        }
                    }

                    function y(e, t) {
                        var n, r = !1;
                        while (n = e.next()) {
                            if ("/" == n && r) {
                                t.tokenize = v;
                                break
                            }
                            r = "*" == n
                        }
                        return g("comment", "comment")
                    }

                    function b(e, t) {
                        var n, r = !1;
                        while (null != (n = e.next())) {
                            if (!r && ("`" == n || "$" == n && e.eat("{"))) {
                                t.tokenize = v;
                                break
                            }
                            r = !r && "\\" == n
                        }
                        return g("quasi", "string-2", e.current())
                    }
                    var w = "([{}])";

                    function x(e, t) {
                        t.fatArrowAt && (t.fatArrowAt = null);
                        var n = e.string.indexOf("=>", e.start);
                        if (!(n < 0)) {
                            if (u) {
                                var r = /:\s*(?:\w+(?:<[^>]*>|\[\])?|\{[^}]*\})\s*$/.exec(e.string.slice(e.start, n));
                                r && (n = r.index)
                            }
                            for (var i = 0, o = !1, l = n - 1; l >= 0; --l) {
                                var a = e.string.charAt(l),
                                    s = w.indexOf(a);
                                if (s >= 0 && s < 3) {
                                    if (!i) {
                                        ++l;
                                        break
                                    }
                                    if (0 == --i) {
                                        "(" == a && (o = !0);
                                        break
                                    }
                                } else if (s >= 3 && s < 6) ++i;
                                else if (c.test(a)) o = !0;
                                else {
                                    if (/["'\/]/.test(a)) return;
                                    if (o && !i) {
                                        ++l;
                                        break
                                    }
                                }
                            }
                            o && !i && (t.fatArrowAt = l)
                        }
                    }
                    var k = {
                        atom: !0,
                        number: !0,
                        variable: !0,
                        string: !0,
                        regexp: !0,
                        this: !0,
                        "jsonld-keyword": !0
                    };

                    function C(e, t, n, r, i, o) {
                        this.indented = e, this.column = t, this.type = n, this.prev = i, this.info = o, null != r && (this.align = r)
                    }

                    function S(e, t) {
                        for (var n = e.localVars; n; n = n.next)
                            if (n.name == t) return !0;
                        for (var r = e.context; r; r = r.prev)
                            for (n = r.vars; n; n = n.next)
                                if (n.name == t) return !0
                    }

                    function L(e, t, n, r, i) {
                        var o = e.cc;
                        T.state = e, T.stream = i, T.marked = null, T.cc = o, T.style = t, e.lexical.hasOwnProperty("align") || (e.lexical.align = !0);
                        while (1) {
                            var l = o.length ? o.pop() : s ? G : _;
                            if (l(n, r)) {
                                while (o.length && o[o.length - 1].lex) o.pop()();
                                return T.marked ? T.marked : "variable" == n && S(e, r) ? "variable-2" : t
                            }
                        }
                    }
                    var T = {
                        state: null,
                        column: null,
                        marked: null,
                        cc: null
                    };

                    function M() {
                        for (var e = arguments.length - 1; e >= 0; e--) T.cc.push(arguments[e])
                    }

                    function N() {
                        return M.apply(null, arguments), !0
                    }

                    function O(e, t) {
                        for (var n = t; n; n = n.next)
                            if (n.name == e) return !0;
                        return !1
                    }

                    function A(e) {
                        var t = T.state;
                        if (T.marked = "def", t.context)
                            if ("var" == t.lexical.info && t.context && t.context.block) {
                                var r = D(e, t.context);
                                if (null != r) return void(t.context = r)
                            } else if (!O(e, t.localVars)) return void(t.localVars = new H(e, t.localVars));
                        n.globalVars && !O(e, t.globalVars) && (t.globalVars = new H(e, t.globalVars))
                    }

                    function D(e, t) {
                        if (t) {
                            if (t.block) {
                                var n = D(e, t.prev);
                                return n ? n == t.prev ? t : new W(n, t.vars, !0) : null
                            }
                            return O(e, t.vars) ? t : new W(t.prev, new H(e, t.vars), !1)
                        }
                        return null
                    }

                    function E(e) {
                        return "public" == e || "private" == e || "protected" == e || "abstract" == e || "readonly" == e
                    }

                    function W(e, t, n) {
                        this.prev = e, this.vars = t, this.block = n
                    }

                    function H(e, t) {
                        this.name = e, this.next = t
                    }
                    var F = new H("this", new H("arguments", null));

                    function I() {
                        T.state.context = new W(T.state.context, T.state.localVars, !1), T.state.localVars = F
                    }

                    function P() {
                        T.state.context = new W(T.state.context, T.state.localVars, !0), T.state.localVars = null
                    }

                    function R() {
                        T.state.localVars = T.state.context.vars, T.state.context = T.state.context.prev
                    }

                    function z(e, t) {
                        var n = function() {
                            var n = T.state,
                                r = n.indented;
                            if ("stat" == n.lexical.type) r = n.lexical.indented;
                            else
                                for (var i = n.lexical; i && ")" == i.type && i.align; i = i.prev) r = i.indented;
                            n.lexical = new C(r, T.stream.column(), e, null, n.lexical, t)
                        };
                        return n.lex = !0, n
                    }

                    function B() {
                        var e = T.state;
                        e.lexical.prev && (")" == e.lexical.type && (e.indented = e.lexical.indented), e.lexical = e.lexical.prev)
                    }

                    function $(e) {
                        function t(n) {
                            return n == e ? N() : ";" == e || "}" == n || ")" == n || "]" == n ? M() : N(t)
                        }
                        return t
                    }

                    function _(e, t) {
                        return "var" == e ? N(z("vardef", t), Ce, $(";"), B) : "keyword a" == e ? N(z("form"), U, _, B) : "keyword b" == e ? N(z("form"), _, B) : "keyword d" == e ? T.stream.match(/^\s*$/, !1) ? N() : N(z("stat"), Y, $(";"), B) : "debugger" == e ? N($(";")) : "{" == e ? N(z("}"), P, fe, B, R) : ";" == e ? N() : "if" == e ? ("else" == T.state.lexical.info && T.state.cc[T.state.cc.length - 1] == B && T.state.cc.pop()(), N(z("form"), U, _, B, Oe)) : "function" == e ? N(We) : "for" == e ? N(z("form"), Ae, _, B) : "class" == e || u && "interface" == t ? (T.marked = "keyword", N(z("form", "class" == e ? e : t), Re, B)) : "variable" == e ? u && "declare" == t ? (T.marked = "keyword", N(_)) : u && ("module" == t || "enum" == t || "type" == t) && T.stream.match(/^\s*\w/, !1) ? (T.marked = "keyword", "enum" == t ? N(qe) : "type" == t ? N(Fe, $("operator"), ge, $(";")) : N(z("form"), Se, $("{"), z("}"), fe, B, B)) : u && "namespace" == t ? (T.marked = "keyword", N(z("form"), G, _, B)) : u && "abstract" == t ? (T.marked = "keyword", N(_)) : N(z("stat"), ie) : "switch" == e ? N(z("form"), U, $("{"), z("}", "switch"), P, fe, B, B, R) : "case" == e ? N(G, $(":")) : "default" == e ? N($(":")) : "catch" == e ? N(z("form"), I, j, _, B, R) : "export" == e ? N(z("stat"), _e, B) : "import" == e ? N(z("stat"), Ge, B) : "async" == e ? N(_) : "@" == t ? N(G, _) : M(z("stat"), G, $(";"), B)
                    }

                    function j(e) {
                        if ("(" == e) return N(Ie, $(")"))
                    }

                    function G(e, t) {
                        return K(e, t, !1)
                    }

                    function V(e, t) {
                        return K(e, t, !0)
                    }

                    function U(e) {
                        return "(" != e ? M() : N(z(")"), G, $(")"), B)
                    }

                    function K(e, t, n) {
                        if (T.state.fatArrowAt == T.stream.start) {
                            var r = n ? ee : Q;
                            if ("(" == e) return N(I, z(")"), ue(Ie, ")"), B, $("=>"), r, R);
                            if ("variable" == e) return M(I, Se, $("=>"), r, R)
                        }
                        var i = n ? q : X;
                        return k.hasOwnProperty(e) ? N(i) : "function" == e ? N(We, i) : "class" == e || u && "interface" == t ? (T.marked = "keyword", N(z("form"), Pe, B)) : "keyword c" == e || "async" == e ? N(n ? V : G) : "(" == e ? N(z(")"), Y, $(")"), B, i) : "operator" == e || "spread" == e ? N(n ? V : G) : "[" == e ? N(z("]"), Xe, B, i) : "{" == e ? ce(le, "}", null, i) : "quasi" == e ? M(J, i) : "new" == e ? N(te(n)) : "import" == e ? N(G) : N()
                    }

                    function Y(e) {
                        return e.match(/[;\}\)\],]/) ? M() : M(G)
                    }

                    function X(e, t) {
                        return "," == e ? N(G) : q(e, t, !1)
                    }

                    function q(e, t, n) {
                        var r = 0 == n ? X : q,
                            i = 0 == n ? G : V;
                        return "=>" == e ? N(I, n ? ee : Q, R) : "operator" == e ? /\+\+|--/.test(t) || u && "!" == t ? N(r) : u && "<" == t && T.stream.match(/^([^>]|<.*?>)*>\s*\(/, !1) ? N(z(">"), ue(ge, ">"), B, r) : "?" == t ? N(G, $(":"), i) : N(i) : "quasi" == e ? M(J, r) : ";" != e ? "(" == e ? ce(V, ")", "call", r) : "." == e ? N(oe, r) : "[" == e ? N(z("]"), Y, $("]"), B, r) : u && "as" == t ? (T.marked = "keyword", N(ge, r)) : "regexp" == e ? (T.state.lastType = T.marked = "operator", T.stream.backUp(T.stream.pos - T.stream.start - 1), N(i)) : void 0 : void 0
                    }

                    function J(e, t) {
                        return "quasi" != e ? M() : "${" != t.slice(t.length - 2) ? N(J) : N(G, Z)
                    }

                    function Z(e) {
                        if ("}" == e) return T.marked = "string-2", T.state.tokenize = b, N(J)
                    }

                    function Q(e) {
                        return x(T.stream, T.state), M("{" == e ? _ : G)
                    }

                    function ee(e) {
                        return x(T.stream, T.state), M("{" == e ? _ : V)
                    }

                    function te(e) {
                        return function(t) {
                            return "." == t ? N(e ? re : ne) : "variable" == t && u ? N(we, e ? q : X) : M(e ? V : G)
                        }
                    }

                    function ne(e, t) {
                        if ("target" == t) return T.marked = "keyword", N(X)
                    }

                    function re(e, t) {
                        if ("target" == t) return T.marked = "keyword", N(q)
                    }

                    function ie(e) {
                        return ":" == e ? N(B, _) : M(X, $(";"), B)
                    }

                    function oe(e) {
                        if ("variable" == e) return T.marked = "property", N()
                    }

                    function le(e, t) {
                        return "async" == e ? (T.marked = "property", N(le)) : "variable" == e || "keyword" == T.style ? (T.marked = "property", "get" == t || "set" == t ? N(ae) : (u && T.state.fatArrowAt == T.stream.start && (n = T.stream.match(/^\s*:\s*/, !1)) && (T.state.fatArrowAt = T.stream.pos + n[0].length), N(se))) : "number" == e || "string" == e ? (T.marked = a ? "property" : T.style + " property", N(se)) : "jsonld-keyword" == e ? N(se) : u && E(t) ? (T.marked = "keyword", N(le)) : "[" == e ? N(G, he, $("]"), se) : "spread" == e ? N(V, se) : "*" == t ? (T.marked = "keyword", N(le)) : ":" == e ? M(se) : void 0;
                        var n
                    }

                    function ae(e) {
                        return "variable" != e ? M(se) : (T.marked = "property", N(We))
                    }

                    function se(e) {
                        return ":" == e ? N(V) : "(" == e ? M(We) : void 0
                    }

                    function ue(e, t, n) {
                        function r(i, o) {
                            if (n ? n.indexOf(i) > -1 : "," == i) {
                                var l = T.state.lexical;
                                return "call" == l.info && (l.pos = (l.pos || 0) + 1), N((function(n, r) {
                                    return n == t || r == t ? M() : M(e)
                                }), r)
                            }
                            return i == t || o == t ? N() : n && n.indexOf(";") > -1 ? M(e) : N($(t))
                        }
                        return function(n, i) {
                            return n == t || i == t ? N() : M(e, r)
                        }
                    }

                    function ce(e, t, n) {
                        for (var r = 3; r < arguments.length; r++) T.cc.push(arguments[r]);
                        return N(z(t, n), ue(e, t), B)
                    }

                    function fe(e) {
                        return "}" == e ? N() : M(_, fe)
                    }

                    function he(e, t) {
                        if (u) {
                            if (":" == e || "in" == t) return N(ge);
                            if ("?" == t) return N(he)
                        }
                    }

                    function de(e) {
                        if (u && ":" == e) return T.stream.match(/^\s*\w+\s+is\b/, !1) ? N(G, pe, ge) : N(ge)
                    }

                    function pe(e, t) {
                        if ("is" == t) return T.marked = "keyword", N()
                    }

                    function ge(e, t) {
                        return "keyof" == t || "typeof" == t || "infer" == t ? (T.marked = "keyword", N("typeof" == t ? V : ge)) : "variable" == e || "void" == t ? (T.marked = "type", N(be)) : "|" == t || "&" == t ? N(ge) : "string" == e || "number" == e || "atom" == e ? N(be) : "[" == e ? N(z("]"), ue(ge, "]", ","), B, be) : "{" == e ? N(z("}"), ue(me, "}", ",;"), B, be) : "(" == e ? N(ue(ye, ")"), ve, be) : "<" == e ? N(ue(ge, ">"), ge) : void 0
                    }

                    function ve(e) {
                        if ("=>" == e) return N(ge)
                    }

                    function me(e, t) {
                        return "variable" == e || "keyword" == T.style ? (T.marked = "property", N(me)) : "?" == t || "number" == e || "string" == e ? N(me) : ":" == e ? N(ge) : "[" == e ? N($("variable"), he, $("]"), me) : "(" == e ? M(He, me) : void 0
                    }

                    function ye(e, t) {
                        return "variable" == e && T.stream.match(/^\s*[?:]/, !1) || "?" == t ? N(ye) : ":" == e ? N(ge) : "spread" == e ? N(ye) : M(ge)
                    }

                    function be(e, t) {
                        return "<" == t ? N(z(">"), ue(ge, ">"), B, be) : "|" == t || "." == e || "&" == t ? N(ge) : "[" == e ? N(ge, $("]"), be) : "extends" == t || "implements" == t ? (T.marked = "keyword", N(ge)) : "?" == t ? N(ge, $(":"), ge) : void 0
                    }

                    function we(e, t) {
                        if ("<" == t) return N(z(">"), ue(ge, ">"), B, be)
                    }

                    function xe() {
                        return M(ge, ke)
                    }

                    function ke(e, t) {
                        if ("=" == t) return N(ge)
                    }

                    function Ce(e, t) {
                        return "enum" == t ? (T.marked = "keyword", N(qe)) : M(Se, he, Me, Ne)
                    }

                    function Se(e, t) {
                        return u && E(t) ? (T.marked = "keyword", N(Se)) : "variable" == e ? (A(t), N()) : "spread" == e ? N(Se) : "[" == e ? ce(Te, "]") : "{" == e ? ce(Le, "}") : void 0
                    }

                    function Le(e, t) {
                        return "variable" != e || T.stream.match(/^\s*:/, !1) ? ("variable" == e && (T.marked = "property"), "spread" == e ? N(Se) : "}" == e ? M() : "[" == e ? N(G, $("]"), $(":"), Le) : N($(":"), Se, Me)) : (A(t), N(Me))
                    }

                    function Te() {
                        return M(Se, Me)
                    }

                    function Me(e, t) {
                        if ("=" == t) return N(V)
                    }

                    function Ne(e) {
                        if ("," == e) return N(Ce)
                    }

                    function Oe(e, t) {
                        if ("keyword b" == e && "else" == t) return N(z("form", "else"), _, B)
                    }

                    function Ae(e, t) {
                        return "await" == t ? N(Ae) : "(" == e ? N(z(")"), De, B) : void 0
                    }

                    function De(e) {
                        return "var" == e ? N(Ce, Ee) : "variable" == e ? N(Ee) : M(Ee)
                    }

                    function Ee(e, t) {
                        return ")" == e ? N() : ";" == e ? N(Ee) : "in" == t || "of" == t ? (T.marked = "keyword", N(G, Ee)) : M(G, Ee)
                    }

                    function We(e, t) {
                        return "*" == t ? (T.marked = "keyword", N(We)) : "variable" == e ? (A(t), N(We)) : "(" == e ? N(I, z(")"), ue(Ie, ")"), B, de, _, R) : u && "<" == t ? N(z(">"), ue(xe, ">"), B, We) : void 0
                    }

                    function He(e, t) {
                        return "*" == t ? (T.marked = "keyword", N(He)) : "variable" == e ? (A(t), N(He)) : "(" == e ? N(I, z(")"), ue(Ie, ")"), B, de, R) : u && "<" == t ? N(z(">"), ue(xe, ">"), B, He) : void 0
                    }

                    function Fe(e, t) {
                        return "keyword" == e || "variable" == e ? (T.marked = "type", N(Fe)) : "<" == t ? N(z(">"), ue(xe, ">"), B) : void 0
                    }

                    function Ie(e, t) {
                        return "@" == t && N(G, Ie), "spread" == e ? N(Ie) : u && E(t) ? (T.marked = "keyword", N(Ie)) : u && "this" == e ? N(he, Me) : M(Se, he, Me)
                    }

                    function Pe(e, t) {
                        return "variable" == e ? Re(e, t) : ze(e, t)
                    }

                    function Re(e, t) {
                        if ("variable" == e) return A(t), N(ze)
                    }

                    function ze(e, t) {
                        return "<" == t ? N(z(">"), ue(xe, ">"), B, ze) : "extends" == t || "implements" == t || u && "," == e ? ("implements" == t && (T.marked = "keyword"), N(u ? ge : G, ze)) : "{" == e ? N(z("}"), Be, B) : void 0
                    }

                    function Be(e, t) {
                        return "async" == e || "variable" == e && ("chen/static/tte/static" == t || "get" == t || "set" == t || u && E(t)) && T.stream.match(/^\s+[\w$\xa1-\uffff]/, !1) ? (T.marked = "keyword", N(Be)) : "variable" == e || "keyword" == T.style ? (T.marked = "property", N(u ? $e : We, Be)) : "number" == e || "string" == e ? N(u ? $e : We, Be) : "[" == e ? N(G, he, $("]"), u ? $e : We, Be) : "*" == t ? (T.marked = "keyword", N(Be)) : u && "(" == e ? M(He, Be) : ";" == e || "," == e ? N(Be) : "}" == e ? N() : "@" == t ? N(G, Be) : void 0
                    }

                    function $e(e, t) {
                        if ("?" == t) return N($e);
                        if (":" == e) return N(ge, Me);
                        if ("=" == t) return N(V);
                        var n = T.state.lexical.prev,
                            r = n && "interface" == n.info;
                        return M(r ? He : We)
                    }

                    function _e(e, t) {
                        return "*" == t ? (T.marked = "keyword", N(Ye, $(";"))) : "default" == t ? (T.marked = "keyword", N(G, $(";"))) : "{" == e ? N(ue(je, "}"), Ye, $(";")) : M(_)
                    }

                    function je(e, t) {
                        return "as" == t ? (T.marked = "keyword", N($("variable"))) : "variable" == e ? M(V, je) : void 0
                    }

                    function Ge(e) {
                        return "string" == e ? N() : "(" == e ? M(G) : M(Ve, Ue, Ye)
                    }

                    function Ve(e, t) {
                        return "{" == e ? ce(Ve, "}") : ("variable" == e && A(t), "*" == t && (T.marked = "keyword"), N(Ke))
                    }

                    function Ue(e) {
                        if ("," == e) return N(Ve, Ue)
                    }

                    function Ke(e, t) {
                        if ("as" == t) return T.marked = "keyword", N(Ve)
                    }

                    function Ye(e, t) {
                        if ("from" == t) return T.marked = "keyword", N(G)
                    }

                    function Xe(e) {
                        return "]" == e ? N() : M(ue(V, "]"))
                    }

                    function qe() {
                        return M(z("form"), Se, $("{"), z("}"), ue(Je, "}"), B, B)
                    }

                    function Je() {
                        return M(Se, Me)
                    }

                    function Ze(e, t) {
                        return "operator" == e.lastType || "," == e.lastType || h.test(t.charAt(0)) || /[,.]/.test(t.charAt(0))
                    }

                    function Qe(e, t, n) {
                        return t.tokenize == v && /^(?:operator|sof|keyword [bcd]|case|new|export|default|spread|[\[{}\(,;:]|=>)$/.test(t.lastType) || "quasi" == t.lastType && /\{\s*$/.test(e.string.slice(0, e.pos - (n || 0)))
                    }
                    return R.lex = !0, B.lex = !0, {
                        startState: function(e) {
                            var t = {
                                tokenize: v,
                                lastType: "sof",
                                cc: [],
                                lexical: new C((e || 0) - o, 0, "block", !1),
                                localVars: n.localVars,
                                context: n.localVars && new W(null, null, !1),
                                indented: e || 0
                            };
                            return n.globalVars && "object" == typeof n.globalVars && (t.globalVars = n.globalVars), t
                        },
                        token: function(e, t) {
                            if (e.sol() && (t.lexical.hasOwnProperty("align") || (t.lexical.align = !1), t.indented = e.indentation(), x(e, t)), t.tokenize != y && e.eatSpace()) return null;
                            var n = t.tokenize(e, t);
                            return "comment" == r ? n : (t.lastType = "operator" != r || "++" != i && "--" != i ? r : "incdec", L(t, n, r, i, e))
                        },
                        indent: function(t, r) {
                            if (t.tokenize == y) return e.Pass;
                            if (t.tokenize != v) return 0;
                            var i, a = r && r.charAt(0),
                                s = t.lexical;
                            if (!/^\s*else\b/.test(r))
                                for (var u = t.cc.length - 1; u >= 0; --u) {
                                    var c = t.cc[u];
                                    if (c == B) s = s.prev;
                                    else if (c != Oe) break
                                }
                            while (("stat" == s.type || "form" == s.type) && ("}" == a || (i = t.cc[t.cc.length - 1]) && (i == X || i == q) && !/^[,\.=+\-*:?[\(]/.test(r))) s = s.prev;
                            l && ")" == s.type && "stat" == s.prev.type && (s = s.prev);
                            var f = s.type,
                                h = a == f;
                            return "vardef" == f ? s.indented + ("operator" == t.lastType || "," == t.lastType ? s.info.length + 1 : 0) : "form" == f && "{" == a ? s.indented : "form" == f ? s.indented + o : "stat" == f ? s.indented + (Ze(t, r) ? l || o : 0) : "switch" != s.info || h || 0 == n.doubleIndentSwitch ? s.align ? s.column + (h ? 0 : 1) : s.indented + (h ? 0 : o) : s.indented + (/^(?:case|default)\b/.test(r) ? o : 2 * o)
                        },
                        electricInput: /^\s*(?:case .*?:|default:|\{|\})$/,
                        blockCommentStart: s ? null : "/*",
                        blockCommentEnd: s ? null : "*/",
                        blockCommentContinue: s ? null : " * ",
                        lineComment: s ? null : "//",
                        fold: "brace",
                        closeBrackets: "()[]{}''\"\"``",
                        helperType: s ? "json" : "javascript",
                        jsonldMode: a,
                        jsonMode: s,
                        expressionAllowed: Qe,
                        skipExpression: function(e) {
                            var t = e.cc[e.cc.length - 1];
                            t != G && t != V || e.cc.pop()
                        }
                    }
                })), e.registerHelper("wordChars", "javascript", /[\w$]/), e.defineMIME("text/javascript", "javascript"), e.defineMIME("text/ecmascript", "javascript"), e.defineMIME("application/javascript", "javascript"), e.defineMIME("application/x-javascript", "javascript"), e.defineMIME("application/ecmascript", "javascript"), e.defineMIME("application/json", {
                    name: "javascript",
                    json: !0
                }), e.defineMIME("application/x-json", {
                    name: "javascript",
                    json: !0
                }), e.defineMIME("application/ld+json", {
                    name: "javascript",
                    jsonld: !0
                }), e.defineMIME("text/typescript", {
                    name: "javascript",
                    typescript: !0
                }), e.defineMIME("application/typescript", {
                    name: "javascript",
                    typescript: !0
                })
            }))
        }
    }
]);