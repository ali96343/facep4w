(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-7c740a14"], {
        "3c34": function(t, e, n) {
            "use strict";
            n.r(e);
            var a = function() {
                    var t = this,
                        e = t.$createElement,
                        n = t._self._c || e;
                    return n("div", {
                        staticClass: "app-container documentation-container"
                    }, [n("a", {
                        staticClass: "document-btn",
                        attrs: {
                            target: "_blank",
                            href: "https://panjiachen.github.io/vue-element-admin-site/"
                        }
                    }, [t._v("Documentation")]), n("a", {
                        staticClass: "document-btn",
                        attrs: {
                            target: "_blank",
                            href: "https://github.com/PanJiaChen/vue-element-admin/"
                        }
                    }, [t._v("Github Repository")]), n("a", {
                        staticClass: "document-btn",
                        attrs: {
                            target: "_blank",
                            href: "https://panjiachen.gitee.io/vue-element-admin-site/zh/"
                        }
                    }, [t._v("国内文档")]), n("dropdown-menu", {
                        staticClass: "document-btn",
                        attrs: {
                            items: t.articleList,
                            title: "系列文章"
                        }
                    }), n("a", {
                        staticClass: "document-btn",
                        attrs: {
                            target: "_blank",
                            href: "https://panjiachen.github.io/vue-element-admin-site/zh/job/"
                        }
                    }, [t._v("内推招聘")])], 1)
                },
                i = [],
                s = n("7c70"),
                c = {
                    name: "Documentation",
                    components: {
                        DropdownMenu: s["a"]
                    },
                    data: function() {
                        return {
                            articleList: [{
                                title: "基础篇",
                                href: "https://juejin.im/post/59097cd7a22b9d0065fb61d2"
                            }, {
                                title: "登录权限篇",
                                href: "https://juejin.im/post/591aa14f570c35006961acac"
                            }, {
                                title: "实战篇",
                                href: "https://juejin.im/post/593121aa0ce4630057f70d35"
                            }, {
                                title: "vue-admin-template 篇",
                                href: "https://juejin.im/post/595b4d776fb9a06bbe7dba56"
                            }, {
                                title: "v4.0 篇",
                                href: "https://juejin.im/post/5c92ff94f265da6128275a85"
                            }, {
                                title: "自行封装 component",
                                href: "https://segmentfault.com/a/1190000009090836"
                            }, {
                                title: "优雅的使用 icon",
                                href: "https://juejin.im/post/59bb864b5188257e7a427c09"
                            }, {
                                title: "webpack4（上）",
                                href: "https://juejin.im/post/59bb864b5188257e7a427c09"
                            }, {
                                title: "webpack4（下）",
                                href: "https://juejin.im/post/5b5d6d6f6fb9a04fea58aabc"
                            }]
                        }
                    }
                },
                r = c,
                u = (n("7f55"), n("2877")),
                o = Object(u["a"])(r, a, i, !1, null, "27229217", null);
            e["default"] = o.exports
        },
        "4ba3": function(t, e, n) {
            "use strict";
            var a = n("7626"),
                i = n.n(a);
            i.a
        },
        7626: function(t, e, n) {},
        "7c70": function(t, e, n) {
            "use strict";
            var a = function() {
                    var t = this,
                        e = t.$createElement,
                        n = t._self._c || e;
                    return n("div", {
                        staticClass: "share-dropdown-menu",
                        class: {
                            active: t.isActive
                        }
                    }, [n("div", {
                        staticClass: "share-dropdown-menu-wrapper"
                    }, [n("span", {
                        staticClass: "share-dropdown-menu-title",
                        on: {
                            click: function(e) {
                                return e.target !== e.currentTarget ? null : t.clickTitle(e)
                            }
                        }
                    }, [t._v(t._s(t.title))]), t._l(t.items, (function(e, a) {
                        return n("div", {
                            key: a,
                            staticClass: "share-dropdown-menu-item"
                        }, [e.href ? n("a", {
                            attrs: {
                                href: e.href,
                                target: "_blank"
                            }
                        }, [t._v(t._s(e.title))]) : n("span", [t._v(t._s(e.title))])])
                    }))], 2)])
                },
                i = [],
                s = {
                    props: {
                        items: {
                            type: Array,
                            default: function() {
                                return []
                            }
                        },
                        title: {
                            type: String,
                            default: "vue"
                        }
                    },
                    data: function() {
                        return {
                            isActive: !1
                        }
                    },
                    methods: {
                        clickTitle: function() {
                            this.isActive = !this.isActive
                        }
                    }
                },
                c = s,
                r = (n("4ba3"), n("2877")),
                u = Object(r["a"])(c, a, i, !1, null, null, null);
            e["a"] = u.exports
        },
        "7f55": function(t, e, n) {
            "use strict";
            var a = n("e648"),
                i = n.n(a);
            i.a
        },
        e648: function(t, e, n) {}
    }
]);