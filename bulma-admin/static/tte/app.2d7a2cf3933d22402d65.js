 !function(e) {
    function t(t) {
        for(var o, i, s=t[0], l=t[1], c=t[2], d=0, u=[]; d<s.length; d++)i=s[d],
        Object.prototype.hasOwnProperty.call(r, i)&&r[i]&&u.push(r[i][0]),
        r[i]=0;
        for(o in l)Object.prototype.hasOwnProperty.call(l, o)&&(e[o]=l[o]);
        for(f&&f(t); u.length; )u.shift()();
        return n.push.apply(n, c||[]),
        a()
    }

    function a() {
        for(var e, t=0; t<n.length; t++) {
            for(var a=n[t], o= !0, s=1; s<a.length; s++) {
                var l=a[s];
                0 !==r[l]&&(o= !1)
            }

            o&&(n.splice(t--, 1), e=i(i.s=a[0]))
        }

        return e
    }

    var o= {}

    ,
    r= {
        0: 0
    }

    ,
    n=[];

    function i(t) {
        if(o[t])return o[t].exports;

        var a=o[t]= {

            i:t,
            l: !1,
            exports: {}
        }

        ;
        return e[t].call(a.exports, a, a.exports, i),
        a.l= !0,
        a.exports
    }

    i.m=e,
    i.c=o,
    i.d=function(e, t, a) {
        i.o(e, t)||Object.defineProperty(e, t, {
                enumerable: !0, get:a
            }

        )
    }

    ,
    i.r=function(e) {
        "undefined" !=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e, Symbol.toStringTag, {
                value:"Module"
            }

        ),
        Object.defineProperty(e, "__esModule", {
                value: !0
            }

        )
    }

    ,
    i.t=function(e, t) {
        if(1&t&&(e=i(e)), 8&t)return e;
        if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;
        var a=Object.create(null);

        if(i.r(a), Object.defineProperty(a, "default", {
                    enumerable: !0, value:e
                }

            ), 2&t&&"string" !=typeof e)for(var o in e)i.d(a, o, function(t) {
                return e[t]
            }

            .bind(null, o));
        return a
    }

    ,
    i.n=function(e) {
        var t=e&&e.__esModule?function() {
            return e.default
        }

        :function() {
            return e
        }

        ;
        return i.d(t, "a", t),
        t
    }

    ,
    i.o=function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }

    ,
    i.p="/bulma-admin-dashboard-template/";
    var s=window.webpackJsonp=window.webpackJsonp||[],
    l=s.push.bind(s);
    s.push=t,
    s=s.slice();
    for(var c=0; c<s.length; c++)t(s[c]);
    var f=l;
    n.push([1, 1]),
    a()
}

([, function(e, t, a) {
        a(2), a(3), a(4)
    }

    , function(e, t, a) {}

    , function(e, t) {
        document.addEventListener("DOMContentLoaded", (function() {
                    var e=Array.prototype.slice.call(document.querySelectorAll(".navbar-burger"), 0); e.length>0&&e.forEach((function(e) {
                                e.addEventListener("click", (function() {
                                            var t=e.dataset.target, a=document.getElementById(t); e.classList.toggle("is-active"), a.classList.toggle("is-active")
                                        }

                                    ))
                            }

                        )); var t=Array.prototype.slice.call(document.querySelectorAll(".is-tab"), 0); if(t.length>0) {
                        t.forEach((function(e) {
                                    e.addEventListener("click", (function() {
                                                t.forEach((function(e) {
                                                            e.classList.remove("is-active")
                                                        }

                                                    )), e.classList.add("is-active")
                                            }

                                        ))
                                }

                            ))
                    }
                }

            ))
    }

    , function(e, t, a) {
        "use strict"; a.r(t); var o=a(0), r= {
            chart: {
                height:350, type:"bar"
            }

            , plotOptions: {
                bar: {
                    dataLabels: {
                        position:"top"
                    }
                }
            }

            , dataLabels: {
                enabled: !0, formatter:function(e) {
                    return e+"%"
                }

                , offsetY:-20, style: {
                    fontSize:"12px", colors:["#f8f8f2"]
                }
            }

            , series:[ {
                name:"Inflation", data:[2.3, 3.1, 4, 10.1, 4, 3.6, 3.2, 2.3, 1.4, .8, .5, .2]
            }

            ], xaxis: {
                categories:["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], position:"top", labels: {
                    offsetY:-18, style: {
                        colors:"#f8f8f2"
                    }
                }

                , axisBorder: {
                    show: !1
                }

                , axisTicks: {
                    show: !1
                }

                , crosshairs: {
                    fill: {
                        type:"gradient", gradient: {
                            colorFrom:"#D8E3F0", colorTo:"#BED1E6", stops:[0, 100], opacityFrom:.4, opacityTo:.5
                        }
                    }
                }

                , tooltip: {
                    enabled: !0, offsetY:-35
                }
            }

            , fill: {
                gradient: {
                    shade:"light", type:"horizontal", shadeIntensity:.25, gradientToColors:void 0, inverseColors: !0, opacityFrom:1, opacityTo:1, stops:[50, 0, 100, 100]
                }
            }

            , yaxis: {
                axisBorder: {
                    show: !1
                }

                , axisTicks: {
                    show: !1
                }

                , labels: {
                    show: !1, formatter:function(e) {
                        return e+"%"
                    }
                }
            }

            , title: {
                text:"Monthly Inflation in Argentina, 2002", floating: !0, offsetY:320, align:"center", style: {
                    color:"#f8f8f2"
                }
            }
        }

        ; new o.a(document.querySelector("#chartBar"), r).render(); function n(e, t, a) {
            for(var o=0, r=[]; o<t; ) {
                var n=Math.floor(Math.random()*(a.max-a.min+1))+a.min; r.push([e, n]), e+=864e5, o++
            }

            return r
        }

        new o.a(document.querySelector("#chartLine"), {
                chart: {
                    height:350, type:"area"
                }

                , dataLabels: {
                    enabled: !1
                }

                , stroke: {
                    curve:"smooth"
                }

                , series:[ {
                    name:"series1", data:[31, 40, 28, 51, 42, 109, 100]
                }

                , {
                    name:"series2", data:[11, 32, 45, 32, 34, 52, 41]
                }

                ], legend: {
                    labels: {
                        colors:"#f8f8f2"
                    }
                }

                , xaxis: {
                    type:"datetime", categories:["2018-09-19T00:00:00", "2018-09-19T01:30:00", "2018-09-19T02:30:00", "2018-09-19T03:30:00", "2018-09-19T04:30:00", "2018-09-19T05:30:00", "2018-09-19T06:30:00"], labels: {
                        style: {
                            colors:"#f8f8f2"
                        }
                    }
                }

                , yaxis: {
                    show: !0, labels: {
                        show: !0, style: {
                            colors:["#f8f8f2"]
                        }
                    }

                    , crosshairs: {
                        show: !0, position:"back", stroke: {
                            color:"#FFF", width:1, dashArray:0
                        }
                    }
                }

                , tooltip: {
                    x: {
                        format:"dd/MM/yy HH:mm"
                    }
                }
            }

        ).render(); var i= {
            chart: {
                height:350, type:"scatter", zoom: {
                    type:"xy"
                }
            }

            , series:[ {
                name:"TEAM 1", data:n(new Date("11 Feb 2017 GMT").getTime(), 20, {
                        min:10, max:60
                    }

                )
            }

            , {
                name:"TEAM 2", data:n(new Date("11 Feb 2017 GMT").getTime(), 20, {
                        min:10, max:60
                    }

                )
            }

            , {
                name:"TEAM 3", data:n(new Date("11 Feb 2017 GMT").getTime(), 30, {
                        min:10, max:60
                    }

                )
            }

            , {
                name:"TEAM 4", data:n(new Date("11 Feb 2017 GMT").getTime(), 10, {
                        min:10, max:60
                    }

                )
            }

            , {
                name:"TEAM 5", data:n(new Date("11 Feb 2017 GMT").getTime(), 30, {
                        min:10, max:60
                    }

                )
            }

            ], legend: {
                labels: {
                    colors:"#f8f8f2"
                }
            }

            , dataLabels: {
                enabled: !1
            }

            , grid: {
                xaxis: {
                    showLines: !0
                }

                , yaxis: {
                    showLines: !0
                }
            }

            , xaxis: {
                type:"datetime", labels: {
                    style: {
                        colors:"#f8f8f2"
                    }
                }
            }

            , yaxis: {
                max:70, labels: {
                    style: {
                        colors:"#f8f8f2"
                    }
                }
            }
        }

        ; new o.a(document.querySelector("#chartScatter"), i).render(); new o.a(document.querySelector("#chartDoughnut"), {
                chart: {
                    height:280, type:"radialBar"
                }

                , series:[67, 84, 97, 61], plotOptions: {
                    radialBar: {
                        dataLabels: {
                            total: {
                                show: !0, label:"TOTAL", color:"#f8f8f2"
                            }

                            , value: {
                                show: !0, color:"#f8f8f2"
                            }
                        }
                    }
                }

                , labels:["TEAM A", "TEAM B", "TEAM C", "TEAM D"]
            }

        ).render()
    }

    ]);