
                /*! Chained 2.0.0-beta.3 - MIT license - Copyright 2010-2017 Mika Tuupola */ ! function(a, b, c, d) {
                    "use strict";
                    a.fn.chained = function(b) {
                        return this.each(function() {
                            function c() {
                                var c = !0,
                                    f = a("option:selected", d).val();
                                a(d).html(e.html());
                                var g = "";
                                a(b).each(function() {
                                    var b = a("option:selected", this).val();
                                    b && (g.length > 0 && (g += "+"), g += b)
                                });
                                var h;
                                h = a.isArray(b) ? a(b[0]).first() : a(b).first();
                                var i = a("option:selected", h).val();
                                a("option", d).each(function() {
                                    if ("" !== a(this).val()) {
                                        var b = [],
                                            d = String(a(this).data("chained"));
                                        d && (b = d.split(" ")), b.indexOf(g) > -1 || b.indexOf(i) > -1 ? a(this).val() === f && (a(this).prop("selected", !0), c = !1) : a(this).remove()
                                    }
                                }), 1 === a("option", d).length && "" === a(d).val() ? a(d).prop("disabled", !0) : a(d).prop("disabled", !1), c && a(d).trigger("change")
                            }
                            var d = this,
                                e = a(d).clone();
                            a(b).each(function() {
                                a(this).bind("change", function() {
                                    c()
                                }), a("option:selected", this).length || a("option", this).first().attr("selected", "selected"), c()
                            })
                        })
                    }, a.fn.chainedTo = a.fn.chained, a.fn.chained.defaults = {}
                }(window.jQuery || window.Zepto, window, document);
