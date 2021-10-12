! function() {
    function t(t, n) {
        if (!(t instanceof n)) throw new TypeError("Cannot call a class as a function")
    }(window.webpackJsonp = window.webpackJsonp || []).push([
        [7], {
            "R+Zu": function(n, o, e) {
                "use strict";
                e.r(o), e.d(o, "TypographyModule", function() {
                    return C
                });
                var c, p, a, r = e("ofXK"),
                    i = e("Wp6s"),
                    b = e("/t3+"),
                    g = e("tyNb"),
                    _ = e("fXoL"),
                    s = e("0MCZ"),
                    h = e("jQpT"),
                    y = [{
                        path: "",
                        component: (c = function n() {
                            t(this, n)
                        }, c.\u0275fac = function(t) {
                            return new(t || c)
                        }, c.\u0275cmp = _.Jb({
                            type: c,
                            selectors: [
                                ["app-typography-page"]
                            ],
                            decls: 78,
                            vars: 0,
                            consts: [
                                ["role", "heading", 1, "page-header"],
                                [1, "typography-content"],
                                [1, "typography-content__wrapper"],
                                [1, "typography-content__item-wrapper"],
                                [1, "typography-content__headings"],
                                [1, "typography-content__colors"],
                                [1, "typography-content__colors_blue"],
                                [1, "typography-content__colors_green"],
                                [1, "typography-content__colors_pink"],
                                [1, "typography-content__colors_yellow"],
                                [1, "typography-content__colors_light-blue"],
                                [1, "typography-content__colors_violet"],
                                [1, "typography-content__settings"],
                                [1, "fw-light"],
                                [1, "fw-medium"],
                                [1, "fw-bold"],
                                [1, "font-uppercase"],
                                [1, "font-lowercase"],
                                [1, "fst-italic"],
                                [1, "typography-content__size"],
                                [1, "fs-sm"],
                                [1, "fs-regular"],
                                [1, "fs-md"],
                                [1, "fs-xl"],
                                [1, "fs-xxl"]
                            ],
                            template: function(t, n) {
                                1 & t && (_.Vb(0, "app-layout"), _.Vb(1, "mat-toolbar", 0), _.Vb(2, "h1"), _.Cc(3, "Typography"), _.Ub(), _.Ub(), _.Vb(4, "mat-card-content", 1), _.Vb(5, "div", 2), _.Vb(6, "mat-card", 3), _.Vb(7, "mat-card-title"), _.Vb(8, "p"), _.Cc(9, "Headings"), _.Ub(), _.Ub(), _.Vb(10, "div", 4), _.Vb(11, "h1"), _.Cc(12, "h1. Heading"), _.Ub(), _.Vb(13, "h2"), _.Cc(14, "h2. Heading"), _.Ub(), _.Vb(15, "h3"), _.Cc(16, "h3. Heading"), _.Ub(), _.Vb(17, "h4"), _.Cc(18, "h4. Heading"), _.Ub(), _.Vb(19, "h5"), _.Cc(20, "h5. Heading"), _.Ub(), _.Vb(21, "h6"), _.Cc(22, "h6. Heading"), _.Ub(), _.Ub(), _.Ub(), _.Vb(23, "mat-card", 3), _.Vb(24, "mat-card-title"), _.Vb(25, "p"), _.Cc(26, "Typography Colors"), _.Ub(), _.Ub(), _.Vb(27, "div", 5), _.Vb(28, "h1", 6), _.Cc(29, "h1. Heading"), _.Ub(), _.Vb(30, "h2", 7), _.Cc(31, "h2. Heading"), _.Ub(), _.Vb(32, "h3", 8), _.Cc(33, "h3. Heading"), _.Ub(), _.Vb(34, "h4", 9), _.Cc(35, "h4. Heading"), _.Ub(), _.Vb(36, "h5", 10), _.Cc(37, "h5. Heading"), _.Ub(), _.Vb(38, "h6", 11), _.Cc(39, "h6. Heading"), _.Ub(), _.Ub(), _.Ub(), _.Ub(), _.Vb(40, "div", 2), _.Vb(41, "mat-card", 3), _.Vb(42, "mat-card-title"), _.Vb(43, "p"), _.Cc(44, "Basic Text Settings"), _.Ub(), _.Ub(), _.Vb(45, "div", 12), _.Vb(46, "p"), _.Cc(47, "Basic text"), _.Ub(), _.Vb(48, "p", 13), _.Cc(49, "Basic light text"), _.Ub(), _.Vb(50, "p", 14), _.Cc(51, "Basic medium text"), _.Ub(), _.Vb(52, "p", 15), _.Cc(53, "Basic bold text"), _.Ub(), _.Vb(54, "p", 16), _.Cc(55, "basic lowercase text"), _.Ub(), _.Vb(56, "p", 17), _.Cc(57, "basic lowercase text"), _.Ub(), _.Vb(58, "p"), _.Cc(59, "Basic Capitalized Text"), _.Ub(), _.Vb(60, "p", 18), _.Cc(61, "Basic Cursive Text"), _.Ub(), _.Ub(), _.Ub(), _.Vb(62, "mat-card", 3), _.Vb(63, "mat-card-title"), _.Vb(64, "p"), _.Cc(65, "Text Size"), _.Ub(), _.Ub(), _.Vb(66, "div", 19), _.Vb(67, "p", 20), _.Cc(68, "Heading Typography SM Font Size"), _.Ub(), _.Vb(69, "p", 21), _.Cc(70, "Heading Typography Regular Font Size"), _.Ub(), _.Vb(71, "p", 22), _.Cc(72, "Heading Typography MD Font Size"), _.Ub(), _.Vb(73, "p", 23), _.Cc(74, "Heading Typography XL Font Size"), _.Ub(), _.Vb(75, "p", 24), _.Cc(76, " Heading Typography XXL Font Size"), _.Ub(), _.Ub(), _.Ub(), _.Ub(), _.Ub(), _.Qb(77, "app-footer"), _.Ub())
                            },
                            directives: [s.a, b.a, i.b, i.a, i.e, h.a],
                            styles: [".typography-content__wrapper[_ngcontent-%COMP%]{display:flex;padding:0 8px}@media (max-width:576px){.typography-content__wrapper[_ngcontent-%COMP%]{flex-wrap:wrap}}.typography-content__item-wrapper[_ngcontent-%COMP%]{box-shadow:0 3px 11px 0 #e8eafc,0 3px 3px -2px hsla(0,0%,69.8%,.10196078431372549),0 1px 8px 0 hsla(0,0%,60.4%,.10196078431372549);width:100%;margin:16px}.typography-content__colors[_ngcontent-%COMP%], .typography-content__headings[_ngcontent-%COMP%], .typography-content__settings[_ngcontent-%COMP%], .typography-content__size[_ngcontent-%COMP%]{margin-top:8px;border:1px dashed #536dfe;padding:32px 16px}@media (max-width:576px){.typography-content__colors[_ngcontent-%COMP%]   h1[_ngcontent-%COMP%], .typography-content__headings[_ngcontent-%COMP%]   h1[_ngcontent-%COMP%], .typography-content__settings[_ngcontent-%COMP%]   h1[_ngcontent-%COMP%], .typography-content__size[_ngcontent-%COMP%]   h1[_ngcontent-%COMP%]{line-height:46px}}.typography-content__colors_blue[_ngcontent-%COMP%]{color:#536dfe}.typography-content__colors_green[_ngcontent-%COMP%]{color:#3cd4a0}.typography-content__colors_pink[_ngcontent-%COMP%]{color:#ff4081}.typography-content__colors_yellow[_ngcontent-%COMP%]{color:#ffc260}.typography-content__colors_light-blue[_ngcontent-%COMP%]{color:#798dfe}.typography-content__colors_violet[_ngcontent-%COMP%]{color:#9013fe}.fw-light[_ngcontent-%COMP%]{font-weight:400}.fw-medium[_ngcontent-%COMP%]{font-weight:500}.fw-bold[_ngcontent-%COMP%]{font-weight:600}.font-uppercase[_ngcontent-%COMP%]{text-transform:uppercase}.font-lowercase[_ngcontent-%COMP%]{text-transform:lowercase}.fst-italic[_ngcontent-%COMP%]{font-style:italic}.fs-sm[_ngcontent-%COMP%]{font-size:11.2px}.fs-regular[_ngcontent-%COMP%]{font-size:14px}.fs-md[_ngcontent-%COMP%]{font-size:21px}.fs-xl[_ngcontent-%COMP%]{font-size:28px}.fs-xxl[_ngcontent-%COMP%]{font-size:42px}"]
                        }), c)
                    }],
                    l = ((p = function n() {
                        t(this, n)
                    }).\u0275fac = function(t) {
                        return new(t || p)
                    }, p.\u0275mod = _.Nb({
                        type: p
                    }), p.\u0275inj = _.Mb({
                        imports: [
                            [g.e.forChild(y)], g.e
                        ]
                    }), p),
                    d = e("PCNd"),
                    C = ((a = function n() {
                        t(this, n)
                    }).\u0275fac = function(t) {
                        return new(t || a)
                    }, a.\u0275mod = _.Nb({
                        type: a
                    }), a.\u0275inj = _.Mb({
                        imports: [
                            [r.c, l, i.c, b.b, d.a]
                        ]
                    }), a)
            }
        }
    ])
}();