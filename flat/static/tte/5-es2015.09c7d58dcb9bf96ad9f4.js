(window.webpackJsonp = window.webpackJsonp || []).push([
    [5], {
        UUPU: function(t, o, n) {
            "use strict";
            n.r(o), n.d(o, "NotificationModule", function() {
                return V
            });
            var e = n("ofXK"),
                i = n("/t3+"),
                c = n("Wp6s"),
                a = n("bTqV"),
                r = n("NFeN"),
                s = n("tyNb"),
                p = n("R0Ic"),
                b = n("5eHb"),
                l = n("fXoL");
            let d = (() => {
                    class t extends b.a {
                        constructor(t, o) {
                            super(t, o), this.toastrService = t, this.toastPackage = o
                        }
                    }
                    return t.\u0275fac = function(o) {
                        return new(o || t)(l.Pb(b.d), l.Pb(b.b))
                    }, t.\u0275cmp = l.Jb({
                        type: t,
                        selectors: [
                            ["app-success-toast"]
                        ],
                        features: [l.Ab],
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
                            1 & t && (l.Vb(0, "div", 0), l.Vb(1, "div", 1), l.Vb(2, "div", 2), l.Vb(3, "mat-icon", 3), l.Cc(4, "done"), l.Ub(), l.Ub(), l.Vb(5, "p", 4), l.Cc(6, "The item was shipped"), l.Ub(), l.Ub(), l.Vb(7, "div", 2), l.Vb(8, "mat-icon", 5), l.cc("click", function() {
                                return o.remove()
                            }), l.Cc(9, "close"), l.Ub(), l.Ub(), l.Ub())
                        },
                        directives: [r.a],
                        styles: [".toastr-wrapper[_ngcontent-%COMP%]{display:flex;justify-content:space-between;align-items:center;width:100%}.toastr-wrapper-icon[_ngcontent-%COMP%]{color:hsla(0,0%,100%,.5019607843137255);height:45px;width:45px;justify-content:center}.toastr-content[_ngcontent-%COMP%], .toastr-wrapper-icon[_ngcontent-%COMP%]{display:flex;align-items:center}.toastr-content__title[_ngcontent-%COMP%]{margin:0}.toastr-icon[_ngcontent-%COMP%]{padding:0;width:auto;height:auto}[_nghost-%COMP%]{position:relative;overflow:hidden;margin:16px 0 6px;pointer-events:all;cursor:pointer;width:257px;color:#fff;display:flex;align-items:center;background-color:#3cd4a0;height:45px}"],
                        data: {
                            animation: [Object(p.m)("flyInOut", [Object(p.j)("inactive", Object(p.k)({
                                opacity: 0
                            })), Object(p.j)("active", Object(p.k)({
                                opacity: 1
                            })), Object(p.j)("removed", Object(p.k)({
                                opacity: 0
                            })), Object(p.l)("inactive => active", Object(p.e)("{{ easeTime }}ms {{ easing }}")), Object(p.l)("active => removed", Object(p.e)("{{ easeTime }}ms {{ easing }}"))])]
                        }
                    }), t
                })(),
                _ = (() => {
                    class t extends b.a {
                        constructor(t, o) {
                            super(t, o), this.toastrService = t, this.toastPackage = o
                        }
                    }
                    return t.\u0275fac = function(o) {
                        return new(o || t)(l.Pb(b.d), l.Pb(b.b))
                    }, t.\u0275cmp = l.Jb({
                        type: t,
                        selectors: [
                            ["app-error-toastr"]
                        ],
                        features: [l.Ab],
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
                            1 & t && (l.Vb(0, "div", 0), l.Vb(1, "div", 1), l.Vb(2, "div", 2), l.Vb(3, "mat-icon", 3), l.Cc(4, "email"), l.Ub(), l.Ub(), l.Vb(5, "p", 4), l.Cc(6, "Message was not sent!"), l.Ub(), l.Ub(), l.Vb(7, "div", 2), l.Vb(8, "mat-icon", 5), l.cc("click", function() {
                                return o.remove()
                            }), l.Cc(9, "close"), l.Ub(), l.Ub(), l.Ub())
                        },
                        directives: [r.a],
                        styles: [".toastr-wrapper[_ngcontent-%COMP%]{display:flex;justify-content:space-between;align-items:center;width:100%}.toastr-wrapper-icon[_ngcontent-%COMP%]{color:hsla(0,0%,100%,.5019607843137255);height:45px;width:45px;justify-content:center}.toastr-content[_ngcontent-%COMP%], .toastr-wrapper-icon[_ngcontent-%COMP%]{display:flex;align-items:center}.toastr-content__title[_ngcontent-%COMP%]{margin:0}.toastr-icon[_ngcontent-%COMP%]{padding:0;width:auto;height:auto}[_nghost-%COMP%]{position:relative;overflow:hidden;margin:16px 0 6px;pointer-events:all;cursor:pointer;width:257px;color:#fff;display:flex;align-items:center;background-color:#ff4081;height:45px}"],
                        data: {
                            animation: [Object(p.m)("flyInOut", [Object(p.j)("inactive", Object(p.k)({
                                opacity: 0
                            })), Object(p.j)("active", Object(p.k)({
                                opacity: 1
                            })), Object(p.j)("removed", Object(p.k)({
                                opacity: 0
                            })), Object(p.l)("inactive => active", Object(p.e)("{{ easeTime }}ms {{ easing }}")), Object(p.l)("active => removed", Object(p.e)("{{ easeTime }}ms {{ easing }}"))])]
                        }
                    }), t
                })(),
                f = (() => {
                    class t extends b.a {
                        constructor(t, o) {
                            super(t, o), this.toastrService = t, this.toastPackage = o
                        }
                    }
                    return t.\u0275fac = function(o) {
                        return new(o || t)(l.Pb(b.d), l.Pb(b.b))
                    }, t.\u0275cmp = l.Jb({
                        type: t,
                        selectors: [
                            ["app-info-toastr"]
                        ],
                        features: [l.Ab],
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
                            1 & t && (l.Vb(0, "div", 0), l.Vb(1, "div", 1), l.Vb(2, "div", 2), l.Vb(3, "mat-icon", 3), l.Cc(4, "announcement"), l.Ub(), l.Ub(), l.Vb(5, "p", 4), l.Cc(6, "New user feedback received"), l.Ub(), l.Ub(), l.Vb(7, "div", 2), l.Vb(8, "mat-icon", 5), l.cc("click", function() {
                                return o.remove()
                            }), l.Cc(9, "close"), l.Ub(), l.Ub(), l.Ub())
                        },
                        directives: [r.a],
                        styles: [".toastr-wrapper[_ngcontent-%COMP%]{display:flex;justify-content:space-between;align-items:center;width:100%}.toastr-wrapper-icon[_ngcontent-%COMP%]{color:hsla(0,0%,100%,.5019607843137255);height:45px;width:45px;justify-content:center}.toastr-content[_ngcontent-%COMP%], .toastr-wrapper-icon[_ngcontent-%COMP%]{display:flex;align-items:center}.toastr-content__title[_ngcontent-%COMP%]{margin:0}.toastr-icon[_ngcontent-%COMP%]{padding:0;width:auto;height:auto}[_nghost-%COMP%]{position:relative;overflow:hidden;margin:16px 0 6px;pointer-events:all;cursor:pointer;width:257px;color:#fff;display:flex;align-items:center;background-color:#536dfe;height:45px}"],
                        data: {
                            animation: [Object(p.m)("flyInOut", [Object(p.j)("inactive", Object(p.k)({
                                opacity: 0
                            })), Object(p.j)("active", Object(p.k)({
                                opacity: 1
                            })), Object(p.j)("removed", Object(p.k)({
                                opacity: 0
                            })), Object(p.l)("inactive => active", Object(p.e)("{{ easeTime }}ms {{ easing }}")), Object(p.l)("active => removed", Object(p.e)("{{ easeTime }}ms {{ easing }}"))])]
                        }
                    }), t
                })();
            var g = n("0MCZ"),
                m = n("jQpT");
            const u = function(t) {
                return {
                    active: t
                }
            };
            var C = function(t) {
                return t.bottomCenter = "toast-bottom-center", t.bottomRight = "toast-bottom-right", t.bottomLeft = "toast-bottom-left", t.topCenter = "toast-top-center", t.topRight = "toast-top-right", t.topLeft = "toast-top-left", t
            }({});
            const w = [{
                path: "",
                component: (() => {
                    class t {
                        constructor(t) {
                            this.toastrService = t, this.toastrPositionTypes = C, this.toastrPosition = this.toastrPositionTypes.topRight, this.timeOut = 3e3, this.toastrLink = "https://github.com/scttcper/ngx-toastr"
                        }
                        setToastrPosition(t) {
                            this.toastrPosition = t
                        }
                        showSuccess() {
                            this.toastrService.show(null, null, {
                                positionClass: this.toastrPosition,
                                toastComponent: d,
                                timeOut: this.timeOut,
                                tapToDismiss: !1
                            })
                        }
                        showErrorToastr() {
                            this.toastrService.show(null, null, {
                                positionClass: this.toastrPosition,
                                toastComponent: _,
                                timeOut: this.timeOut,
                                tapToDismiss: !1
                            })
                        }
                        showInfoToastr() {
                            this.toastrService.show(null, null, {
                                positionClass: this.toastrPosition,
                                toastComponent: f,
                                timeOut: this.timeOut,
                                tapToDismiss: !1
                            })
                        }
                    }
                    return t.\u0275fac = function(o) {
                        return new(o || t)(l.Pb(b.d))
                    }, t.\u0275cmp = l.Jb({
                        type: t,
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
                            1 & t && (l.Vb(0, "app-layout"), l.Vb(1, "mat-toolbar", 0), l.Vb(2, "h1"), l.Cc(3, "Notifications"), l.Ub(), l.Ub(), l.Vb(4, "div", 1), l.Vb(5, "mat-card", 2), l.Vb(6, "div", 3), l.Vb(7, "mat-card-title"), l.Vb(8, "p"), l.Cc(9, "Layout Options"), l.Ub(), l.Ub(), l.Vb(10, "mat-card-subtitle"), l.Vb(11, "p"), l.Cc(12, "There are few position options available for notifications. You can click any of them to change notifications position:"), l.Ub(), l.Ub(), l.Vb(13, "mat-card-content"), l.Vb(14, "div", 4), l.Vb(15, "div", 5), l.Vb(16, "button", 6), l.cc("click", function() {
                                return o.setToastrPosition(o.toastrPositionTypes.topLeft)
                            }), l.Ub(), l.Vb(17, "button", 7), l.cc("click", function() {
                                return o.setToastrPosition(o.toastrPositionTypes.topCenter)
                            }), l.Ub(), l.Vb(18, "button", 6), l.cc("click", function() {
                                return o.setToastrPosition(o.toastrPositionTypes.topRight)
                            }), l.Ub(), l.Ub(), l.Vb(19, "p", 8), l.Cc(20, "Click any position"), l.Ub(), l.Vb(21, "div", 5), l.Vb(22, "button", 9), l.cc("click", function() {
                                return o.setToastrPosition(o.toastrPositionTypes.bottomLeft)
                            }), l.Ub(), l.Vb(23, "button", 10), l.cc("click", function() {
                                return o.setToastrPosition(o.toastrPositionTypes.bottomCenter)
                            }), l.Ub(), l.Vb(24, "button", 9), l.cc("click", function() {
                                return o.setToastrPosition(o.toastrPositionTypes.bottomRight)
                            }), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Vb(25, "div", 3), l.Vb(26, "mat-card-title"), l.Vb(27, "p"), l.Cc(28, "Notifications Types"), l.Ub(), l.Ub(), l.Vb(29, "mat-card-subtitle"), l.Vb(30, "p"), l.Cc(31, "Different types of notifications for lost of use cases. Custom classes are also supported."), l.Ub(), l.Ub(), l.Vb(32, "mat-card-content"), l.Vb(33, "div", 11), l.Vb(34, "button", 12), l.cc("click", function() {
                                return o.showInfoToastr()
                            }), l.Cc(35, "Info Message"), l.Ub(), l.Vb(36, "button", 13), l.cc("click", function() {
                                return o.showErrorToastr()
                            }), l.Cc(37, "Error + Retry Message"), l.Ub(), l.Vb(38, "button", 14), l.cc("click", function() {
                                return o.showSuccess()
                            }), l.Cc(39, "Success Message"), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Vb(40, "div", 3), l.Vb(41, "mat-card-title"), l.Vb(42, "p"), l.Cc(43, "Usage"), l.Ub(), l.Ub(), l.Vb(44, "mat-card-subtitle"), l.Vb(45, "p"), l.Cc(46, "Notifications are created with the help of "), l.Vb(47, "a", 15), l.Cc(48, "ngx-toastr"), l.Ub(), l.Ub(), l.Ub(), l.Vb(49, "mat-card-content", 16), l.Vb(50, "pre", 17), l.Vb(51, "code", 18), l.Cc(52), l.Ub(), l.Cc(53, "\n          "), l.Ub(), l.Vb(54, "p"), l.Cc(55, "For more API information refer to the library documentation"), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Vb(56, "div", 19), l.Vb(57, "mat-card", 20), l.Vb(58, "mat-card-title"), l.Vb(59, "p"), l.Cc(60, "Notification Types Examples"), l.Ub(), l.Ub(), l.Vb(61, "mat-card-content"), l.Vb(62, "div", 21), l.Vb(63, "div", 22), l.Vb(64, "mat-icon"), l.Cc(65, "email"), l.Ub(), l.Ub(), l.Vb(66, "p", 23), l.Cc(67, "Thanks for Checking out Messenger"), l.Ub(), l.Ub(), l.Vb(68, "div", 24), l.Vb(69, "div", 22), l.Vb(70, "mat-icon"), l.Cc(71, "announcement"), l.Ub(), l.Ub(), l.Vb(72, "p", 23), l.Cc(73, "New user feedback received"), l.Ub(), l.Ub(), l.Vb(74, "div", 25), l.Vb(75, "div", 22), l.Vb(76, "mat-icon"), l.Cc(77, "account_box"), l.Ub(), l.Ub(), l.Vb(78, "p", 23), l.Cc(79, "New customer is registered"), l.Ub(), l.Ub(), l.Vb(80, "div", 26), l.Vb(81, "div", 22), l.Vb(82, "mat-icon"), l.Cc(83, "done"), l.Ub(), l.Ub(), l.Vb(84, "p", 23), l.Cc(85, "The order was shipped"), l.Ub(), l.Ub(), l.Vb(86, "div", 24), l.Vb(87, "div", 22), l.Vb(88, "mat-icon"), l.Cc(89, "business_center"), l.Ub(), l.Ub(), l.Vb(90, "p", 23), l.Cc(91, "The order was delivered"), l.Ub(), l.Ub(), l.Vb(92, "div", 27), l.Vb(93, "div", 22), l.Vb(94, "mat-icon"), l.Cc(95, "info"), l.Ub(), l.Ub(), l.Vb(96, "p", 23), l.Cc(97, "5 Defence alerts"), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Vb(98, "mat-card", 20), l.Vb(99, "mat-card-title"), l.Vb(100, "p"), l.Cc(101, "Notification Types Examples"), l.Ub(), l.Ub(), l.Vb(102, "mat-card-content"), l.Vb(103, "div", 28), l.Vb(104, "div", 29), l.Vb(105, "mat-icon"), l.Cc(106, "report"), l.Ub(), l.Ub(), l.Vb(107, "p", 30), l.Cc(108, "New report has been received"), l.Ub(), l.Ub(), l.Vb(109, "div", 31), l.Vb(110, "div", 32), l.Vb(111, "mat-icon"), l.Cc(112, "announcement"), l.Ub(), l.Ub(), l.Vb(113, "p", 30), l.Cc(114, "New user feedback received"), l.Ub(), l.Ub(), l.Vb(115, "div", 33), l.Vb(116, "div", 34), l.Vb(117, "mat-icon"), l.Cc(118, "done"), l.Ub(), l.Ub(), l.Vb(119, "p", 30), l.Cc(120, "The item was shipped"), l.Ub(), l.Ub(), l.Vb(121, "div", 35), l.Vb(122, "div", 36), l.Vb(123, "mat-icon"), l.Cc(124, "email"), l.Ub(), l.Ub(), l.Vb(125, "p", 30), l.Cc(126, "The new message from user @nahawaii"), l.Ub(), l.Ub(), l.Vb(127, "div", 31), l.Vb(128, "div", 32), l.Vb(129, "mat-icon", 37), l.Cc(130, "get_app"), l.Ub(), l.Ub(), l.Vb(131, "p", 30), l.Cc(132, "Your file is ready to upload"), l.Ub(), l.Ub(), l.Vb(133, "div", 38), l.Vb(134, "div", 39), l.Vb(135, "mat-icon"), l.Cc(136, "disc_full"), l.Ub(), l.Ub(), l.Vb(137, "p", 30), l.Cc(138, "The disc is full"), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Vb(139, "mat-card", 20), l.Vb(140, "mat-card-title"), l.Vb(141, "p"), l.Cc(142, "Notification Types Examples"), l.Ub(), l.Ub(), l.Vb(143, "mat-card-content"), l.Vb(144, "div", 40), l.Vb(145, "div", 41), l.Vb(146, "mat-icon"), l.Cc(147, "report"), l.Ub(), l.Ub(), l.Vb(148, "p", 30), l.Cc(149, "New report has been received"), l.Ub(), l.Ub(), l.Vb(150, "div", 40), l.Vb(151, "div", 42), l.Vb(152, "mat-icon"), l.Cc(153, "announcement"), l.Ub(), l.Ub(), l.Vb(154, "p", 30), l.Cc(155, "New user feedback received"), l.Ub(), l.Ub(), l.Vb(156, "div", 40), l.Vb(157, "div", 43), l.Vb(158, "mat-icon"), l.Cc(159, "done"), l.Ub(), l.Ub(), l.Vb(160, "p", 30), l.Cc(161, "The item was shipped"), l.Ub(), l.Ub(), l.Vb(162, "div", 40), l.Vb(163, "div", 44), l.Vb(164, "mat-icon"), l.Cc(165, "email"), l.Ub(), l.Ub(), l.Vb(166, "p", 30), l.Cc(167, "The new message from user @nahawaii"), l.Ub(), l.Ub(), l.Vb(168, "div", 40), l.Vb(169, "div", 42), l.Vb(170, "mat-icon", 37), l.Cc(171, "get_app"), l.Ub(), l.Ub(), l.Vb(172, "p", 30), l.Cc(173, "Your file is ready to upload"), l.Ub(), l.Ub(), l.Vb(174, "div", 40), l.Vb(175, "div", 45), l.Vb(176, "mat-icon"), l.Cc(177, "disc_full"), l.Ub(), l.Ub(), l.Vb(178, "p", 30), l.Cc(179, "The disc is full"), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Ub(), l.Qb(180, "app-footer"), l.Ub()), 2 & t && (l.Db(16), l.lc("ngClass", l.oc(17, u, o.toastrPosition === o.toastrPositionTypes.topLeft)), l.Db(1), l.lc("ngClass", l.oc(19, u, o.toastrPosition === o.toastrPositionTypes.topCenter)), l.Db(1), l.lc("ngClass", l.oc(21, u, o.toastrPosition === o.toastrPositionTypes.topRight)), l.Db(4), l.lc("ngClass", l.oc(23, u, o.toastrPosition === o.toastrPositionTypes.bottomLeft)), l.Db(1), l.lc("ngClass", l.oc(25, u, o.toastrPosition === o.toastrPositionTypes.bottomCenter)), l.Db(1), l.lc("ngClass", l.oc(27, u, o.toastrPosition === o.toastrPositionTypes.bottomRight)), l.Db(23), l.lc("href", o.toastrLink, l.wc), l.Db(5), l.Gc(["\nimport ", "{", " ToastrService ", "}", " from 'ngx-toastr';\n\n@Component(", "{", "...", "}", ")\n  export class YourComponent ", "{", "\n  constructor(private toastr: ToastrService) ", "{", "", "}", "\n\n  showSuccess() ", "{", "\n    this.toastr.success(\n      'Hello world!', 'Toastr fun!'\n    );\n  ", "}", "\n", "}", "\n"]))
                        },
                        directives: [g.a, i.a, c.a, c.e, c.d, c.b, e.j, a.b, r.a, m.a],
                        styles: [".page-content[_ngcontent-%COMP%]{padding:0 8px}.page-content__item-wrapper[_ngcontent-%COMP%], .page-content__items-wrapper[_ngcontent-%COMP%]{display:flex;justify-content:space-around}@media (max-width:576px){.page-content__items-wrapper[_ngcontent-%COMP%]{flex-wrap:wrap}}.page-content__first-item-wrapper[_ngcontent-%COMP%]{display:flex;box-shadow:0 3px 11px 0 #e8eafc,0 3px 3px -2px hsla(0,0%,69.8%,.10196078431372549),0 1px 8px 0 hsla(0,0%,60.4%,.10196078431372549)}@media (max-width:576px){.page-content__first-item-wrapper[_ngcontent-%COMP%]{flex-wrap:wrap;padding-bottom:0}}.page-content__first-item-element[_ngcontent-%COMP%]{width:100%;padding:8px}@media (max-width:576px){.page-content__first-item-element[_ngcontent-%COMP%]{padding:0 0 16px}}.page-content__item[_ngcontent-%COMP%]{box-shadow:0 3px 11px 0 #e8eafc,0 3px 3px -2px hsla(0,0%,69.8%,.10196078431372549),0 1px 8px 0 hsla(0,0%,60.4%,.10196078431372549);width:100%}.select-position[_ngcontent-%COMP%]{width:80%;height:200px;border:1px dashed #536dfe;margin-top:16px;display:flex;flex-direction:column;justify-content:space-between}@media (max-width:576px){.select-position[_ngcontent-%COMP%]{width:100%}}.select-position__items-wrapper[_ngcontent-%COMP%]{width:100%;height:50px;display:flex}.select-position__center-bottom-item[_ngcontent-%COMP%], .select-position__center-top-item[_ngcontent-%COMP%], .select-position__item[_ngcontent-%COMP%], .select-position__item-bottom[_ngcontent-%COMP%], .select-position__item-top[_ngcontent-%COMP%]{cursor:pointer;width:100%;height:100%;background-color:#f3f5ff;border:0;outline:none}.active.select-position__center-bottom-item[_ngcontent-%COMP%], .active.select-position__center-top-item[_ngcontent-%COMP%], .active.select-position__item-bottom[_ngcontent-%COMP%], .active.select-position__item-top[_ngcontent-%COMP%], .select-position__item.active[_ngcontent-%COMP%]{background-color:#c0caff;cursor:default}.select-position__center-top-item[_ngcontent-%COMP%]{border:1px dashed #536dfe;border-top:none}.select-position__center-bottom-item[_ngcontent-%COMP%]{border:1px dashed #536dfe;border-bottom:none}.select-position__item-top[_ngcontent-%COMP%]{border:none;border-bottom:1px dashed #536dfe}.select-position__item-bottom[_ngcontent-%COMP%]{border:none;border-top:1px dashed #536dfe}.select-position__title[_ngcontent-%COMP%]{text-align:center;margin:0;color:#c0caff;font-size:21px;font-weight:400}.mat-card-content[_ngcontent-%COMP%] > [_ngcontent-%COMP%]:last-child.position-buttons-wrapper{margin-top:33px}.position-button[_ngcontent-%COMP%]{display:block;color:#fff;margin-bottom:8px}.position-button_blue[_ngcontent-%COMP%]{background-color:#536dfe}.position-button_pink[_ngcontent-%COMP%]{background-color:#ff4081}.position-button_green[_ngcontent-%COMP%]{background-color:#3cd4a0}.code-block[_ngcontent-%COMP%]{margin-top:50px}@media (max-width:576px){.code-block[_ngcontent-%COMP%]{margin-top:33px}}.code-wrapper[_ngcontent-%COMP%]{margin-top:49px;font-size:11.2px;display:block;overflow-x:auto;padding:7px;color:#4a4a4a;background:#f3f5ff;height:277px;overflow-y:hidden}.code[_ngcontent-%COMP%]{text-wrap:none}.link[_ngcontent-%COMP%]{color:#536dfe}.notification[_ngcontent-%COMP%]{width:100%;display:flex;align-items:center;margin-top:16px;height:45px;border-radius:45px}.notification_solid-pink[_ngcontent-%COMP%]{background-color:#ff4081}.notification_solid-blue[_ngcontent-%COMP%]{background-color:#536dfe}.notification_solid-green[_ngcontent-%COMP%]{background-color:#3cd4a0}.notification_solid-yellow[_ngcontent-%COMP%]{background-color:#ffc260}.notification_solid-violet[_ngcontent-%COMP%]{background-color:#9013fe}.notification_transparent-pink[_ngcontent-%COMP%]{background-color:rgba(255,92,147,.15)}.notification_transparent-blue[_ngcontent-%COMP%]{background-color:rgba(83,109,254,.15)}.notification_transparent-green[_ngcontent-%COMP%]{background-color:rgba(60,212,160,.15)}.notification_transparent-yellow[_ngcontent-%COMP%]{background-color:rgba(255,194,96,.15)}.notification_transparent-violet[_ngcontent-%COMP%]{background-color:rgba(144,19,254,.15)}.notification__title[_ngcontent-%COMP%]{margin:0}.notification__title_white[_ngcontent-%COMP%]{color:#fff}.notification__icon-wrapper[_ngcontent-%COMP%]{height:45px;width:45px;display:flex;align-items:center;justify-content:center}.notification__icon-wrapper_transparent[_ngcontent-%COMP%]{color:hsla(0,0%,100%,.5019607843137255)}.notification__icon-wrapper_transparent-pink[_ngcontent-%COMP%]{color:#ff4081}.notification__icon-wrapper_transparent-blue[_ngcontent-%COMP%]{color:#536dfe}.notification__icon-wrapper_transparent-green[_ngcontent-%COMP%]{color:#3cd4a0}.notification__icon-wrapper_transparent-yellow[_ngcontent-%COMP%]{color:#ffc260}.notification__icon-wrapper_transparent-violet[_ngcontent-%COMP%]{color:#9013fe}.notification__icon-wrapper_solid-pink[_ngcontent-%COMP%]{color:#ff4081}.notification__icon-wrapper_solid-blue[_ngcontent-%COMP%]{color:#536dfe}.notification__icon-wrapper_solid-green[_ngcontent-%COMP%]{color:#3cd4a0}.notification__icon-wrapper_solid-yellow[_ngcontent-%COMP%]{color:#ffc260}.notification__icon-wrapper_solid-violet[_ngcontent-%COMP%]{color:#9013fe}.notification__icon-wrapper-circle[_ngcontent-%COMP%]{height:45px;width:45px;display:flex;align-items:center;justify-content:center;border-radius:45px;margin-right:16px}.notification__icon-wrapper-circle_transparent-pink[_ngcontent-%COMP%]{color:#ff4081;background-color:rgba(255,92,147,.15)}.notification__icon-wrapper-circle_transparent-blue[_ngcontent-%COMP%]{color:#536dfe;background-color:rgba(83,109,254,.15)}.notification__icon-wrapper-circle_transparent-green[_ngcontent-%COMP%]{color:#3cd4a0;background-color:rgba(60,212,160,.15)}.notification__icon-wrapper-circle_transparent-yellow[_ngcontent-%COMP%]{color:#ffc260;background-color:rgba(255,194,96,.15)}.notification__icon-wrapper-circle_transparent-violet[_ngcontent-%COMP%]{color:#9013fe;background-color:rgba(144,19,254,.15)}.icon-rotate[_ngcontent-%COMP%]{transform:rotate(180deg)}"]
                    }), t
                })()
            }];
            let h = (() => {
                class t {}
                return t.\u0275fac = function(o) {
                    return new(o || t)
                }, t.\u0275mod = l.Nb({
                    type: t
                }), t.\u0275inj = l.Mb({
                    imports: [
                        [s.e.forChild(w)], s.e
                    ]
                }), t
            })();
            var U = n("PCNd");
            let V = (() => {
                class t {}
                return t.\u0275fac = function(o) {
                    return new(o || t)
                }, t.\u0275mod = l.Nb({
                    type: t
                }), t.\u0275inj = l.Mb({
                    imports: [
                        [e.c, h, i.b, c.c, a.c, r.b, U.a]
                    ]
                }), t
            })()
        }
    }
]);