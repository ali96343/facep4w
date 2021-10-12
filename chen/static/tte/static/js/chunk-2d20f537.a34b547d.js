(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d20f537"], {
        b2c4: function(a, e, t) {
            "use strict";
            t.r(e);
            var n = function() {
                    var a = this,
                        e = a.$createElement,
                        t = a._self._c || e;
                    return t("div", {
                        staticClass: "app-container"
                    }, [t("div", {
                        staticStyle: {
                            margin: "0 0 5px 20px"
                        }
                    }, [a._v(" Fixed header, sorted by header order, ")]), t("fixed-thead"), t("div", {
                        staticStyle: {
                            margin: "30px 0 5px 20px"
                        }
                    }, [a._v(" Not fixed header, sorted by click order ")]), t("unfixed-thead")], 1)
                },
                l = [],
                r = function() {
                    var a = this,
                        e = a.$createElement,
                        t = a._self._c || e;
                    return t("div", {
                        staticClass: "app-container"
                    }, [t("div", {
                        staticClass: "filter-container"
                    }, [t("el-checkbox-group", {
                        model: {
                            value: a.checkboxVal,
                            callback: function(e) {
                                a.checkboxVal = e
                            },
                            expression: "checkboxVal"
                        }
                    }, [t("el-checkbox", {
                        attrs: {
                            label: "apple"
                        }
                    }, [a._v(" apple ")]), t("el-checkbox", {
                        attrs: {
                            label: "banana"
                        }
                    }, [a._v(" banana ")]), t("el-checkbox", {
                        attrs: {
                            label: "orange"
                        }
                    }, [a._v(" orange ")])], 1)], 1), t("el-table", {
                        key: a.key,
                        staticStyle: {
                            width: "100%"
                        },
                        attrs: {
                            data: a.tableData,
                            border: "",
                            fit: "",
                            "highlight-current-row": ""
                        }
                    }, [t("el-table-column", {
                        attrs: {
                            prop: "name",
                            label: "fruitName",
                            width: "180"
                        }
                    }), a._l(a.formThead, (function(e) {
                        return t("el-table-column", {
                            key: e,
                            attrs: {
                                label: e
                            },
                            scopedSlots: a._u([{
                                key: "default",
                                fn: function(t) {
                                    return [a._v(" " + a._s(t.row[e]) + " ")]
                                }
                            }], null, !0)
                        })
                    }))], 2)], 1)
                },
                o = [],
                c = (t("4de4"), ["apple", "banana"]),
                i = {
                    data: function() {
                        return {
                            tableData: [{
                                name: "fruit-1",
                                apple: "apple-10",
                                banana: "banana-10",
                                orange: "orange-10"
                            }, {
                                name: "fruit-2",
                                apple: "apple-20",
                                banana: "banana-20",
                                orange: "orange-20"
                            }],
                            key: 1,
                            formTheadOptions: ["apple", "banana", "orange"],
                            checkboxVal: c,
                            formThead: c
                        }
                    },
                    watch: {
                        checkboxVal: function(a) {
                            this.formThead = this.formTheadOptions.filter((function(e) {
                                return a.indexOf(e) >= 0
                            })), this.key = this.key + 1
                        }
                    }
                },
                s = i,
                p = t("2877"),
                b = Object(p["a"])(s, r, o, !1, null, null, null),
                u = b.exports,
                d = function() {
                    var a = this,
                        e = a.$createElement,
                        t = a._self._c || e;
                    return t("div", {
                        staticClass: "app-container"
                    }, [t("div", {
                        staticClass: "filter-container"
                    }, [t("el-checkbox-group", {
                        model: {
                            value: a.formThead,
                            callback: function(e) {
                                a.formThead = e
                            },
                            expression: "formThead"
                        }
                    }, [t("el-checkbox", {
                        attrs: {
                            label: "apple"
                        }
                    }, [a._v(" apple ")]), t("el-checkbox", {
                        attrs: {
                            label: "banana"
                        }
                    }, [a._v(" banana ")]), t("el-checkbox", {
                        attrs: {
                            label: "orange"
                        }
                    }, [a._v(" orange ")])], 1)], 1), t("el-table", {
                        staticStyle: {
                            width: "100%"
                        },
                        attrs: {
                            data: a.tableData,
                            border: "",
                            fit: "",
                            "highlight-current-row": ""
                        }
                    }, [t("el-table-column", {
                        attrs: {
                            prop: "name",
                            label: "fruitName",
                            width: "180"
                        }
                    }), a._l(a.formThead, (function(e) {
                        return t("el-table-column", {
                            key: e,
                            attrs: {
                                label: e
                            },
                            scopedSlots: a._u([{
                                key: "default",
                                fn: function(t) {
                                    return [a._v(" " + a._s(t.row[e]) + " ")]
                                }
                            }], null, !0)
                        })
                    }))], 2)], 1)
                },
                h = [],
                f = {
                    data: function() {
                        return {
                            tableData: [{
                                name: "fruit-1",
                                apple: "apple-10",
                                banana: "banana-10",
                                orange: "orange-10"
                            }, {
                                name: "fruit-2",
                                apple: "apple-20",
                                banana: "banana-20",
                                orange: "orange-20"
                            }],
                            formThead: ["apple", "banana"]
                        }
                    }
                },
                m = f,
                x = Object(p["a"])(m, d, h, !1, null, null, null),
                k = x.exports,
                v = {
                    name: "DynamicTable",
                    components: {
                        FixedThead: u,
                        UnfixedThead: k
                    }
                },
                _ = v,
                g = Object(p["a"])(_, n, l, !1, null, null, null);
            e["default"] = g.exports
        }
    }
]);