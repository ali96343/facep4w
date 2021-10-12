! function() {
    function t(t, o) {
        for (var n = 0; n < o.length; n++) {
            var e = o[n];
            e.enumerable = e.enumerable || !1, e.configurable = !0, "value" in e && (e.writable = !0), Object.defineProperty(t, e.key, e)
        }
    }

    function o(t, o) {
        if (!(t instanceof o)) throw new TypeError("Cannot call a class as a function")
    }

    function n(t, o) {
        if ("function" != typeof o && null !== o) throw new TypeError("Super expression must either be null or a function");
        t.prototype = Object.create(o && o.prototype, {
            constructor: {
                value: t,
                writable: !0,
                configurable: !0
            }
        }), o && e(t, o)
    }

    function e(t, o) {
        return (e = Object.setPrototypeOf || function(t, o) {
            return t.__proto__ = o, t
        })(t, o)
    }

    function i(t) {
        var o = function() {
            if ("undefined" == typeof Reflect || !Reflect.construct) return !1;
            if (Reflect.construct.sham) return !1;
            if ("function" == typeof Proxy) return !0;
            try {
                return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {})), !0
            } catch (t) {
                return !1
            }
        }();
        return function() {
            var n, e = r(t);
            if (o) {
                var i = r(this).constructor;
                n = Reflect.construct(e, arguments, i)
            } else n = e.apply(this, arguments);
            return c(this, n)
        }
    }

    function c(t, o) {
        return !o || "object" != typeof o && "function" != typeof o ? function(t) {
            if (void 0 === t) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
            return t
        }(t) : o
    }

    function r(t) {
        return (r = Object.setPrototypeOf ? Object.getPrototypeOf : function(t) {
            return t.__proto__ || Object.getPrototypeOf(t)
        })(t)
    }(window.webpackJsonp = window.webpackJsonp || []).push([
        [5], {
            UUPU: function(e, c, r) {
                "use strict";
                r.r(c), r.d(c, "NotificationModule", function() {
                    return N
                });
                var a, s, p, b, l, f, _ = r("ofXK"),
                    d = r("/t3+"),
                    u = r("Wp6s"),
                    g = r("bTqV"),
                    m = r("NFeN"),
                    C = r("tyNb"),
                    h = r("R0Ic"),
                    w = r("5eHb"),
                    v = r("fXoL"),
                    U = ((p = function(t) {
                        n(c, t);
                        var e = i(c);

                        function c(t, n) {
                            var i;
                            return o(this, c), (i = e.call(this, t, n)).toastrService = t, i.toastPackage = n, i
                        }
                        return c
                    }(w.a)).\u0275fac = function(t) {
                        return new(t || p)(v.Pb(w.d), v.Pb(w.b))
                    }, p.\u0275cmp = v.Jb({
                        type: p,
                        selectors: [
                            ["app-success-toast"]
                        ],
                        features: [v.Ab],
                        decls: 10,
                        vars: 0,
                        consts: [
                            [1, "toastr-wrapper"],
                            [1, "toastr-content"],
                            [1, "toastr-wrapper-icon"],
                            [1, "toastr-icon"],
                            [1, "toastr-content__title"],
                            [1, "toastr-icon", 3, "click"]
                        ],
                        template: function(t, o) {
                            1 & t && (v.Vb(0, "div", 0), v.Vb(1, "div", 1), v.Vb(2, "div", 2), v.Vb(3, "mat-icon", 3), v.Cc(4, "done"), v.Ub(), v.Ub(), v.Vb(5, "p", 4), v.Cc(6, "The item was shipped"), v.Ub(), v.Ub(), v.Vb(7, "div", 2), v.Vb(8, "mat-icon", 5), v.cc("click", function() {
                                return o.remove()
                            }), v.Cc(9, "close"), v.Ub(), v.Ub(), v.Ub())
                        },
                        directives: [m.a],
                        styles: [".toastr-wrapper[_ngcontent-%COMP%]{display:flex;justify-content:space-between;align-items:center;width:100%}.toastr-wrapper-icon[_ngcontent-%COMP%]{color:hsla(0,0%,100%,.5019607843137255);height:45px;width:45px;justify-content:center}.toastr-content[_ngcontent-%COMP%], .toastr-wrapper-icon[_ngcontent-%COMP%]{display:flex;align-items:center}.toastr-content__title[_ngcontent-%COMP%]{margin:0}.toastr-icon[_ngcontent-%COMP%]{padding:0;width:auto;height:auto}[_nghost-%COMP%]{position:relative;overflow:hidden;margin:16px 0 6px;pointer-events:all;cursor:pointer;width:257px;color:#fff;display:flex;align-items:center;background-color:#3cd4a0;height:45px}"],
                        data: {
                            animation: [Object(h.m)("flyInOut", [Object(h.j)("inactive", Object(h.k)({
                                opacity: 0
                            })), Object(h.j)("active", Object(h.k)({
                                opacity: 1
                            })), Object(h.j)("removed", Object(h.k)({
                                opacity: 0
                            })), Object(h.l)("inactive => active", Object(h.e)("{{ easeTime }}ms {{ easing }}")), Object(h.l)("active => removed", Object(h.e)("{{ easeTime }}ms {{ easing }}"))])]
                        }
                    }), p),
                    V = ((s = function(t) {
                        n(c, t);
                        var e = i(c);

                        function c(t, n) {
                            var i;
                            return o(this, c), (i = e.call(this, t, n)).toastrService = t, i.toastPackage = n, i
                        }
                        return c
                    }(w.a)).\u0275fac = function(t) {
                        return new(t || s)(v.Pb(w.d), v.Pb(w.b))
                    }, s.\u0275cmp = v.Jb({
                        type: s,
                        selectors: [
                            ["app-error-toastr"]
                        ],
                        features: [v.Ab],
                        decls: 10,
                        vars: 0,
                        consts: [
                            [1, "toastr-wrapper"],
                            [1, "toastr-content"],
                            [1, "toastr-wrapper-icon"],
                            [1, "toastr-icon"],
                            [1, "toastr-content__title"],
                            [1, "toastr-icon", 3, "click"]
                        ],
                        template: function(t, o) {
                            1 & t && (v.Vb(0, "div", 0), v.Vb(1, "div", 1), v.Vb(2, "div", 2), v.Vb(3, "mat-icon", 3), v.Cc(4, "email"), v.Ub(), v.Ub(), v.Vb(5, "p", 4), v.Cc(6, "Message was not sent!"), v.Ub(), v.Ub(), v.Vb(7, "div", 2), v.Vb(8, "mat-icon", 5), v.cc("click", function() {
                                return o.remove()
                            }), v.Cc(9, "close"), v.Ub(), v.Ub(), v.Ub())
                        },
                        directives: [m.a],
                        styles: [".toastr-wrapper[_ngcontent-%COMP%]{display:flex;justify-content:space-between;align-items:center;width:100%}.toastr-wrapper-icon[_ngcontent-%COMP%]{color:hsla(0,0%,100%,.5019607843137255);height:45px;width:45px;justify-content:center}.toastr-content[_ngcontent-%COMP%], .toastr-wrapper-icon[_ngcontent-%COMP%]{display:flex;align-items:center}.toastr-content__title[_ngcontent-%COMP%]{margin:0}.toastr-icon[_ngcontent-%COMP%]{padding:0;width:auto;height:auto}[_nghost-%COMP%]{position:relative;overflow:hidden;margin:16px 0 6px;pointer-events:all;cursor:pointer;width:257px;color:#fff;display:flex;align-items:center;background-color:#ff4081;height:45px}"],
                        data: {
                            animation: [Object(h.m)("flyInOut", [Object(h.j)("inactive", Object(h.k)({
                                opacity: 0
                            })), Object(h.j)("active", Object(h.k)({
                                opacity: 1
                            })), Object(h.j)("removed", Object(h.k)({
                                opacity: 0
                            })), Object(h.l)("inactive => active", Object(h.e)("{{ easeTime }}ms {{ easing }}")), Object(h.l)("active => removed", Object(h.e)("{{ easeTime }}ms {{ easing }}"))])]
                        }
                    }), s),
                    O = ((a = function(t) {
                        n(c, t);
                        var e = i(c);

                        function c(t, n) {
                            var i;
                            return o(this, c), (i = e.call(this, t, n)).toastrService = t, i.toastPackage = n, i
                        }
                        return c
                    }(w.a)).\u0275fac = function(t) {
                        return new(t || a)(v.Pb(w.d), v.Pb(w.b))
                    }, a.\u0275cmp = v.Jb({
                        type: a,
                        selectors: [
                            ["app-info-toastr"]
                        ],
                        features: [v.Ab],
                        decls: 10,
                        vars: 0,
                        consts: [
                            [1, "toastr-wrapper"],
                            [1, "toastr-content"],
                            [1, "toastr-wrapper-icon"],
                            [1, "toastr-icon"],
                            [1, "toastr-content__title"],
                            [1, "toastr-icon", 3, "click"]
                        ],
                        template: function(t, o) {
                            1 & t && (v.Vb(0, "div", 0), v.Vb(1, "div", 1), v.Vb(2, "div", 2), v.Vb(3, "mat-icon", 3), v.Cc(4, "announcement"), v.Ub(), v.Ub(), v.Vb(5, "p", 4), v.Cc(6, "New user feedback received"), v.Ub(), v.Ub(), v.Vb(7, "div", 2), v.Vb(8, "mat-icon", 5), v.cc("click", function() {
                                return o.remove()
                            }), v.Cc(9, "close"), v.Ub(), v.Ub(), v.Ub())
                        },
                        directives: [m.a],
                        styles: [".toastr-wrapper[_ngcontent-%COMP%]{display:flex;justify-content:space-between;align-items:center;width:100%}.toastr-wrapper-icon[_ngcontent-%COMP%]{color:hsla(0,0%,100%,.5019607843137255);height:45px;width:45px;justify-content:center}.toastr-content[_ngcontent-%COMP%], .toastr-wrapper-icon[_ngcontent-%COMP%]{display:flex;align-items:center}.toastr-content__title[_ngcontent-%COMP%]{margin:0}.toastr-icon[_ngcontent-%COMP%]{padding:0;width:auto;height:auto}[_nghost-%COMP%]{position:relative;overflow:hidden;margin:16px 0 6px;pointer-events:all;cursor:pointer;width:257px;color:#fff;display:flex;align-items:center;background-color:#536dfe;height:45px}"],
                        data: {
                            animation: [Object(h.m)("flyInOut", [Object(h.j)("inactive", Object(h.k)({
                                opacity: 0
                            })), Object(h.j)("active", Object(h.k)({
                                opacity: 1
                            })), Object(h.j)("removed", Object(h.k)({
                                opacity: 0
                            })), Object(h.l)("inactive => active", Object(h.e)("{{ easeTime }}ms {{ easing }}")), Object(h.l)("active => removed", Object(h.e)("{{ easeTime }}ms {{ easing }}"))])]
                        }
                    }), a),
                    P = r("0MCZ"),
                    y = r("jQpT"),
                    x = function(t) {
                        return {
                            active: t
                        }
                    },
                    M = function(t) {
                        return t.bottomCenter = "toast-bottom-center", t.bottomRight = "toast-bottom-right", t.bottomLeft = "toast-bottom-left", t.topCenter = "toast-top-center", t.topRight = "toast-top-right", t.topLeft = "toast-top-left", t
                    }({}),
                    k = [{
                        path: "",
                        component: (b = function() {
                            function n(t) {
                                o(this, n), this.toastrService = t, this.toastrPositionTypes = M, this.toastrPosition = this.toastrPositionTypes.topRight, this.timeOut = 3e3, this.toastrLink = "https://github.com/scttcper/ngx-toastr"
                            }
                            var e, i, c;
                            return e = n, (i = [{
                                key: "setToastrPosition",
                                value: function(t) {
                                    this.toastrPosition = t
                                }
                            }, {
                                key: "showSuccess",
                                value: function() {
                                    this.toastrService.show(null, null, {
                                        positionClass: this.toastrPosition,
                                        toastComponent: U,
                                        timeOut: this.timeOut,
                                        tapToDismiss: !1
                                    })
                                }
                            }, {
                                key: "showErrorToastr",
                                value: function() {
                                    this.toastrService.show(null, null, {
                                        positionClass: this.toastrPosition,
                                        toastComponent: V,
                                        timeOut: this.timeOut,
                                        tapToDismiss: !1
                                    })
                                }
                            }, {
                                key: "showInfoToastr",
                                value: function() {
                                    this.toastrService.show(null, null, {
                                        positionClass: this.toastrPosition,
                                        toastComponent: O,
                                        timeOut: this.timeOut,
                                        tapToDismiss: !1
                                    })
                                }
                            }]) && t(e.prototype, i), c && t(e, c), n
                        }(), b.\u0275fac = function(t) {
                            return new(t || b)(v.Pb(w.d))
                        }, b.\u0275cmp = v.Jb({
                            type: b,
                            selectors: [
                                ["app-notification-page"]
                            ],
                            decls: 181,
                            vars: 29,
                            consts: [
                                ["role", "heading", 1, "page-header"],
                                [1, "page-content"],
                                [1, "page-content__first-item-wrapper"],
                                [1, "page-content__first-item-element"],
                                [1, "select-position"],
                                [1, "select-position__items-wrapper"],
                                [1, "select-position__item-top", 3, "ngClass", "click"],
                                [1, "select-position__center-top-item", 3, "ngClass", "click"],
                                [1, "select-position__title"],
                                [1, "select-position__item-bottom", 3, "ngClass", "click"],
                                [1, "select-position__center-bottom-item", 3, "ngClass", "click"],
                                [1, "position-buttons-wrapper"],
                                ["mat-raised-button", "", 1, "position-button", "position-button_blue", 3, "click"],
                                ["mat-raised-button", "", 1, "position-button", "position-button_pink", 3, "click"],
                                ["mat-raised-button", "", 1, "position-button", "position-button_green", 3, "click"],
                                [1, "link", 3, "href"],
                                [1, "code-block"],
                                [1, "code-wrapper"],
                                [1, "code"],
                                [1, "page-content__items-wrapper"],
                                [1, "page-content__item"],
                                [1, "notification", "notification_solid-pink"],
                                [1, "notification__icon-wrapper", "notification__icon-wrapper_transparent"],
                                [1, "notification__title", "notification__title_white"],
                                [1, "notification", "notification_solid-blue"],
                                [1, "notification", "notification_solid-green"],
                                [1, "notification", "notification_solid-yellow"],
                                [1, "notification", "notification_solid-violet"],
                                [1, "notification", "notification_transparent-pink"],
                                [1, "notification__icon-wrapper", "notification__icon-wrapper_solid-pink"],
                                [1, "notification__title"],
                                [1, "notification", "notification_transparent-blue"],
                                [1, "notification__icon-wrapper", "notification__icon-wrapper_solid-blue"],
                                [1, "notification", "notification_transparent-green"],
                                [1, "notification__icon-wrapper", "notification__icon-wrapper_solid-green"],
                                [1, "notification", "notification_transparent-yellow"],
                                [1, "notification__icon-wrapper", "notification__icon-wrapper_solid-yellow"],
                                [1, "icon-rotate"],
                                [1, "notification", "notification_transparent-violet"],
                                [1, "notification__icon-wrapper", "notification__icon-wrapper_solid-violet"],
                                [1, "notification"],
                                [1, "notification__icon-wrapper-circle", "notification__icon-wrapper-circle_transparent-pink"],
                                [1, "notification__icon-wrapper-circle", "notification__icon-wrapper-circle_transparent-blue"],
                                [1, "notification__icon-wrapper-circle", "notification__icon-wrapper-circle_transparent-green"],
                                [1, "notification__icon-wrapper-circle", "notification__icon-wrapper-circle_transparent-yellow"],
                                [1, "notification__icon-wrapper-circle", "notification__icon-wrapper-circle_transparent-violet"]
                            ],
                            template: function(t, o) {
                                1 & t && (v.Vb(0, "app-layout"), v.Vb(1, "mat-toolbar", 0), v.Vb(2, "h1"), v.Cc(3, "Notifications"), v.Ub(), v.Ub(), v.Vb(4, "div", 1), v.Vb(5, "mat-card", 2), v.Vb(6, "div", 3), v.Vb(7, "mat-card-title"), v.Vb(8, "p"), v.Cc(9, "Layout Options"), v.Ub(), v.Ub(), v.Vb(10, "mat-card-subtitle"), v.Vb(11, "p"), v.Cc(12, "There are few position options available for notifications. You can click any of them to change notifications position:"), v.Ub(), v.Ub(), v.Vb(13, "mat-card-content"), v.Vb(14, "div", 4), v.Vb(15, "div", 5), v.Vb(16, "button", 6), v.cc("click", function() {
                                    return o.setToastrPosition(o.toastrPositionTypes.topLeft)
                                }), v.Ub(), v.Vb(17, "button", 7), v.cc("click", function() {
                                    return o.setToastrPosition(o.toastrPositionTypes.topCenter)
                                }), v.Ub(), v.Vb(18, "button", 6), v.cc("click", function() {
                                    return o.setToastrPosition(o.toastrPositionTypes.topRight)
                                }), v.Ub(), v.Ub(), v.Vb(19, "p", 8), v.Cc(20, "Click any position"), v.Ub(), v.Vb(21, "div", 5), v.Vb(22, "button", 9), v.cc("click", function() {
                                    return o.setToastrPosition(o.toastrPositionTypes.bottomLeft)
                                }), v.Ub(), v.Vb(23, "button", 10), v.cc("click", function() {
                                    return o.setToastrPosition(o.toastrPositionTypes.bottomCenter)
                                }), v.Ub(), v.Vb(24, "button", 9), v.cc("click", function() {
                                    return o.setToastrPosition(o.toastrPositionTypes.bottomRight)
                                }), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Vb(25, "div", 3), v.Vb(26, "mat-card-title"), v.Vb(27, "p"), v.Cc(28, "Notifications Types"), v.Ub(), v.Ub(), v.Vb(29, "mat-card-subtitle"), v.Vb(30, "p"), v.Cc(31, "Different types of notifications for lost of use cases. Custom classes are also supported."), v.Ub(), v.Ub(), v.Vb(32, "mat-card-content"), v.Vb(33, "div", 11), v.Vb(34, "button", 12), v.cc("click", function() {
                                    return o.showInfoToastr()
                                }), v.Cc(35, "Info Message"), v.Ub(), v.Vb(36, "button", 13), v.cc("click", function() {
                                    return o.showErrorToastr()
                                }), v.Cc(37, "Error + Retry Message"), v.Ub(), v.Vb(38, "button", 14), v.cc("click", function() {
                                    return o.showSuccess()
                                }), v.Cc(39, "Success Message"), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Vb(40, "div", 3), v.Vb(41, "mat-card-title"), v.Vb(42, "p"), v.Cc(43, "Usage"), v.Ub(), v.Ub(), v.Vb(44, "mat-card-subtitle"), v.Vb(45, "p"), v.Cc(46, "Notifications are created with the help of "), v.Vb(47, "a", 15), v.Cc(48, "ngx-toastr"), v.Ub(), v.Ub(), v.Ub(), v.Vb(49, "mat-card-content", 16), v.Vb(50, "pre", 17), v.Vb(51, "code", 18), v.Cc(52), v.Ub(), v.Cc(53, "\n          "), v.Ub(), v.Vb(54, "p"), v.Cc(55, "For more API information refer to the library documentation"), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Vb(56, "div", 19), v.Vb(57, "mat-card", 20), v.Vb(58, "mat-card-title"), v.Vb(59, "p"), v.Cc(60, "Notification Types Examples"), v.Ub(), v.Ub(), v.Vb(61, "mat-card-content"), v.Vb(62, "div", 21), v.Vb(63, "div", 22), v.Vb(64, "mat-icon"), v.Cc(65, "email"), v.Ub(), v.Ub(), v.Vb(66, "p", 23), v.Cc(67, "Thanks for Checking out Messenger"), v.Ub(), v.Ub(), v.Vb(68, "div", 24), v.Vb(69, "div", 22), v.Vb(70, "mat-icon"), v.Cc(71, "announcement"), v.Ub(), v.Ub(), v.Vb(72, "p", 23), v.Cc(73, "New user feedback received"), v.Ub(), v.Ub(), v.Vb(74, "div", 25), v.Vb(75, "div", 22), v.Vb(76, "mat-icon"), v.Cc(77, "account_box"), v.Ub(), v.Ub(), v.Vb(78, "p", 23), v.Cc(79, "New customer is registered"), v.Ub(), v.Ub(), v.Vb(80, "div", 26), v.Vb(81, "div", 22), v.Vb(82, "mat-icon"), v.Cc(83, "done"), v.Ub(), v.Ub(), v.Vb(84, "p", 23), v.Cc(85, "The order was shipped"), v.Ub(), v.Ub(), v.Vb(86, "div", 24), v.Vb(87, "div", 22), v.Vb(88, "mat-icon"), v.Cc(89, "business_center"), v.Ub(), v.Ub(), v.Vb(90, "p", 23), v.Cc(91, "The order was delivered"), v.Ub(), v.Ub(), v.Vb(92, "div", 27), v.Vb(93, "div", 22), v.Vb(94, "mat-icon"), v.Cc(95, "info"), v.Ub(), v.Ub(), v.Vb(96, "p", 23), v.Cc(97, "5 Defence alerts"), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Vb(98, "mat-card", 20), v.Vb(99, "mat-card-title"), v.Vb(100, "p"), v.Cc(101, "Notification Types Examples"), v.Ub(), v.Ub(), v.Vb(102, "mat-card-content"), v.Vb(103, "div", 28), v.Vb(104, "div", 29), v.Vb(105, "mat-icon"), v.Cc(106, "report"), v.Ub(), v.Ub(), v.Vb(107, "p", 30), v.Cc(108, "New report has been received"), v.Ub(), v.Ub(), v.Vb(109, "div", 31), v.Vb(110, "div", 32), v.Vb(111, "mat-icon"), v.Cc(112, "announcement"), v.Ub(), v.Ub(), v.Vb(113, "p", 30), v.Cc(114, "New user feedback received"), v.Ub(), v.Ub(), v.Vb(115, "div", 33), v.Vb(116, "div", 34), v.Vb(117, "mat-icon"), v.Cc(118, "done"), v.Ub(), v.Ub(), v.Vb(119, "p", 30), v.Cc(120, "The item was shipped"), v.Ub(), v.Ub(), v.Vb(121, "div", 35), v.Vb(122, "div", 36), v.Vb(123, "mat-icon"), v.Cc(124, "email"), v.Ub(), v.Ub(), v.Vb(125, "p", 30), v.Cc(126, "The new message from user @nahawaii"), v.Ub(), v.Ub(), v.Vb(127, "div", 31), v.Vb(128, "div", 32), v.Vb(129, "mat-icon", 37), v.Cc(130, "get_app"), v.Ub(), v.Ub(), v.Vb(131, "p", 30), v.Cc(132, "Your file is ready to upload"), v.Ub(), v.Ub(), v.Vb(133, "div", 38), v.Vb(134, "div", 39), v.Vb(135, "mat-icon"), v.Cc(136, "disc_full"), v.Ub(), v.Ub(), v.Vb(137, "p", 30), v.Cc(138, "The disc is full"), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Vb(139, "mat-card", 20), v.Vb(140, "mat-card-title"), v.Vb(141, "p"), v.Cc(142, "Notification Types Examples"), v.Ub(), v.Ub(), v.Vb(143, "mat-card-content"), v.Vb(144, "div", 40), v.Vb(145, "div", 41), v.Vb(146, "mat-icon"), v.Cc(147, "report"), v.Ub(), v.Ub(), v.Vb(148, "p", 30), v.Cc(149, "New report has been received"), v.Ub(), v.Ub(), v.Vb(150, "div", 40), v.Vb(151, "div", 42), v.Vb(152, "mat-icon"), v.Cc(153, "announcement"), v.Ub(), v.Ub(), v.Vb(154, "p", 30), v.Cc(155, "New user feedback received"), v.Ub(), v.Ub(), v.Vb(156, "div", 40), v.Vb(157, "div", 43), v.Vb(158, "mat-icon"), v.Cc(159, "done"), v.Ub(), v.Ub(), v.Vb(160, "p", 30), v.Cc(161, "The item was shipped"), v.Ub(), v.Ub(), v.Vb(162, "div", 40), v.Vb(163, "div", 44), v.Vb(164, "mat-icon"), v.Cc(165, "email"), v.Ub(), v.Ub(), v.Vb(166, "p", 30), v.Cc(167, "The new message from user @nahawaii"), v.Ub(), v.Ub(), v.Vb(168, "div", 40), v.Vb(169, "div", 42), v.Vb(170, "mat-icon", 37), v.Cc(171, "get_app"), v.Ub(), v.Ub(), v.Vb(172, "p", 30), v.Cc(173, "Your file is ready to upload"), v.Ub(), v.Ub(), v.Vb(174, "div", 40), v.Vb(175, "div", 45), v.Vb(176, "mat-icon"), v.Cc(177, "disc_full"), v.Ub(), v.Ub(), v.Vb(178, "p", 30), v.Cc(179, "The disc is full"), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Ub(), v.Qb(180, "app-footer"), v.Ub()), 2 & t && (v.Db(16), v.lc("ngClass", v.oc(17, x, o.toastrPosition === o.toastrPositionTypes.topLeft)), v.Db(1), v.lc("ngClass", v.oc(19, x, o.toastrPosition === o.toastrPositionTypes.topCenter)), v.Db(1), v.lc("ngClass", v.oc(21, x, o.toastrPosition === o.toastrPositionTypes.topRight)), v.Db(4), v.lc("ngClass", v.oc(23, x, o.toastrPosition === o.toastrPositionTypes.bottomLeft)), v.Db(1), v.lc("ngClass", v.oc(25, x, o.toastrPosition === o.toastrPositionTypes.bottomCenter)), v.Db(1), v.lc("ngClass", v.oc(27, x, o.toastrPosition === o.toastrPositionTypes.bottomRight)), v.Db(23), v.lc("href", o.toastrLink, v.wc), v.Db(5), v.Gc(["\nimport ", "{", " ToastrService ", "}", " from 'ngx-toastr';\n\n@Component(", "{", "...", "}", ")\n  export class YourComponent ", "{", "\n  constructor(private toastr: ToastrService) ", "{", "", "}", "\n\n  showSuccess() ", "{", "\n    this.toastr.success(\n      'Hello world!', 'Toastr fun!'\n    );\n  ", "}", "\n", "}", "\n"]))
                            },
                            directives: [P.a, d.a, u.a, u.e, u.d, u.b, _.j, g.b, m.a, y.a],
                            styles: [".page-content[_ngcontent-%COMP%]{padding:0 8px}.page-content__item-wrapper[_ngcontent-%COMP%], .page-content__items-wrapper[_ngcontent-%COMP%]{display:flex;justify-content:space-around}@media (max-width:576px){.page-content__items-wrapper[_ngcontent-%COMP%]{flex-wrap:wrap}}.page-content__first-item-wrapper[_ngcontent-%COMP%]{display:flex;box-shadow:0 3px 11px 0 #e8eafc,0 3px 3px -2px hsla(0,0%,69.8%,.10196078431372549),0 1px 8px 0 hsla(0,0%,60.4%,.10196078431372549)}@media (max-width:576px){.page-content__first-item-wrapper[_ngcontent-%COMP%]{flex-wrap:wrap;padding-bottom:0}}.page-content__first-item-element[_ngcontent-%COMP%]{width:100%;padding:8px}@media (max-width:576px){.page-content__first-item-element[_ngcontent-%COMP%]{padding:0 0 16px}}.page-content__item[_ngcontent-%COMP%]{box-shadow:0 3px 11px 0 #e8eafc,0 3px 3px -2px hsla(0,0%,69.8%,.10196078431372549),0 1px 8px 0 hsla(0,0%,60.4%,.10196078431372549);width:100%}.select-position[_ngcontent-%COMP%]{width:80%;height:200px;border:1px dashed #536dfe;margin-top:16px;display:flex;flex-direction:column;justify-content:space-between}@media (max-width:576px){.select-position[_ngcontent-%COMP%]{width:100%}}.select-position__items-wrapper[_ngcontent-%COMP%]{width:100%;height:50px;display:flex}.select-position__center-bottom-item[_ngcontent-%COMP%], .select-position__center-top-item[_ngcontent-%COMP%], .select-position__item[_ngcontent-%COMP%], .select-position__item-bottom[_ngcontent-%COMP%], .select-position__item-top[_ngcontent-%COMP%]{cursor:pointer;width:100%;height:100%;background-color:#f3f5ff;border:0;outline:none}.active.select-position__center-bottom-item[_ngcontent-%COMP%], .active.select-position__center-top-item[_ngcontent-%COMP%], .active.select-position__item-bottom[_ngcontent-%COMP%], .active.select-position__item-top[_ngcontent-%COMP%], .select-position__item.active[_ngcontent-%COMP%]{background-color:#c0caff;cursor:default}.select-position__center-top-item[_ngcontent-%COMP%]{border:1px dashed #536dfe;border-top:none}.select-position__center-bottom-item[_ngcontent-%COMP%]{border:1px dashed #536dfe;border-bottom:none}.select-position__item-top[_ngcontent-%COMP%]{border:none;border-bottom:1px dashed #536dfe}.select-position__item-bottom[_ngcontent-%COMP%]{border:none;border-top:1px dashed #536dfe}.select-position__title[_ngcontent-%COMP%]{text-align:center;margin:0;color:#c0caff;font-size:21px;font-weight:400}.mat-card-content[_ngcontent-%COMP%] > [_ngcontent-%COMP%]:last-child.position-buttons-wrapper{margin-top:33px}.position-button[_ngcontent-%COMP%]{display:block;color:#fff;margin-bottom:8px}.position-button_blue[_ngcontent-%COMP%]{background-color:#536dfe}.position-button_pink[_ngcontent-%COMP%]{background-color:#ff4081}.position-button_green[_ngcontent-%COMP%]{background-color:#3cd4a0}.code-block[_ngcontent-%COMP%]{margin-top:50px}@media (max-width:576px){.code-block[_ngcontent-%COMP%]{margin-top:33px}}.code-wrapper[_ngcontent-%COMP%]{margin-top:49px;font-size:11.2px;display:block;overflow-x:auto;padding:7px;color:#4a4a4a;background:#f3f5ff;height:277px;overflow-y:hidden}.code[_ngcontent-%COMP%]{text-wrap:none}.link[_ngcontent-%COMP%]{color:#536dfe}.notification[_ngcontent-%COMP%]{width:100%;display:flex;align-items:center;margin-top:16px;height:45px;border-radius:45px}.notification_solid-pink[_ngcontent-%COMP%]{background-color:#ff4081}.notification_solid-blue[_ngcontent-%COMP%]{background-color:#536dfe}.notification_solid-green[_ngcontent-%COMP%]{background-color:#3cd4a0}.notification_solid-yellow[_ngcontent-%COMP%]{background-color:#ffc260}.notification_solid-violet[_ngcontent-%COMP%]{background-color:#9013fe}.notification_transparent-pink[_ngcontent-%COMP%]{background-color:rgba(255,92,147,.15)}.notification_transparent-blue[_ngcontent-%COMP%]{background-color:rgba(83,109,254,.15)}.notification_transparent-green[_ngcontent-%COMP%]{background-color:rgba(60,212,160,.15)}.notification_transparent-yellow[_ngcontent-%COMP%]{background-color:rgba(255,194,96,.15)}.notification_transparent-violet[_ngcontent-%COMP%]{background-color:rgba(144,19,254,.15)}.notification__title[_ngcontent-%COMP%]{margin:0}.notification__title_white[_ngcontent-%COMP%]{color:#fff}.notification__icon-wrapper[_ngcontent-%COMP%]{height:45px;width:45px;display:flex;align-items:center;justify-content:center}.notification__icon-wrapper_transparent[_ngcontent-%COMP%]{color:hsla(0,0%,100%,.5019607843137255)}.notification__icon-wrapper_transparent-pink[_ngcontent-%COMP%]{color:#ff4081}.notification__icon-wrapper_transparent-blue[_ngcontent-%COMP%]{color:#536dfe}.notification__icon-wrapper_transparent-green[_ngcontent-%COMP%]{color:#3cd4a0}.notification__icon-wrapper_transparent-yellow[_ngcontent-%COMP%]{color:#ffc260}.notification__icon-wrapper_transparent-violet[_ngcontent-%COMP%]{color:#9013fe}.notification__icon-wrapper_solid-pink[_ngcontent-%COMP%]{color:#ff4081}.notification__icon-wrapper_solid-blue[_ngcontent-%COMP%]{color:#536dfe}.notification__icon-wrapper_solid-green[_ngcontent-%COMP%]{color:#3cd4a0}.notification__icon-wrapper_solid-yellow[_ngcontent-%COMP%]{color:#ffc260}.notification__icon-wrapper_solid-violet[_ngcontent-%COMP%]{color:#9013fe}.notification__icon-wrapper-circle[_ngcontent-%COMP%]{height:45px;width:45px;display:flex;align-items:center;justify-content:center;border-radius:45px;margin-right:16px}.notification__icon-wrapper-circle_transparent-pink[_ngcontent-%COMP%]{color:#ff4081;background-color:rgba(255,92,147,.15)}.notification__icon-wrapper-circle_transparent-blue[_ngcontent-%COMP%]{color:#536dfe;background-color:rgba(83,109,254,.15)}.notification__icon-wrapper-circle_transparent-green[_ngcontent-%COMP%]{color:#3cd4a0;background-color:rgba(60,212,160,.15)}.notification__icon-wrapper-circle_transparent-yellow[_ngcontent-%COMP%]{color:#ffc260;background-color:rgba(255,194,96,.15)}.notification__icon-wrapper-circle_transparent-violet[_ngcontent-%COMP%]{color:#9013fe;background-color:rgba(144,19,254,.15)}.icon-rotate[_ngcontent-%COMP%]{transform:rotate(180deg)}"]
                        }), b)
                    }],
                    j = ((l = function t() {
                        o(this, t)
                    }).\u0275fac = function(t) {
                        return new(t || l)
                    }, l.\u0275mod = v.Nb({
                        type: l
                    }), l.\u0275inj = v.Mb({
                        imports: [
                            [C.e.forChild(k)], C.e
                        ]
                    }), l),
                    T = r("PCNd"),
                    N = ((f = function t() {
                        o(this, t)
                    }).\u0275fac = function(t) {
                        return new(t || f)
                    }, f.\u0275mod = v.Nb({
                        type: f
                    }), f.\u0275inj = v.Mb({
                        imports: [
                            [_.c, j, d.b, u.c, g.c, m.b, T.a]
                        ]
                    }), f)
            }
        }
    ])
}();