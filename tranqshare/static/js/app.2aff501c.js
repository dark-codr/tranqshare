(self.webpackChunkpython_webpack_boilerplate=self.webpackChunkpython_webpack_boilerplate||[]).push([[143],{262:function(e,t,n){"use strict";var d=n(450),o=n.n(d),s=n(306),i=n(51);n(689),window.htmx=o(),window.document.addEventListener("DOMContentLoaded",(function(){window.console.log("dom ready 1")})),window.Alpine=s.Z,s.Z.data("lang_drop",(function(){return{openMenu:!1,deposit:!1,lang:!1,copy:!1,toggleOpen(){this.openMenu=!this.openMenu;const e=document.getElementById("lang"),t=document.getElementById("lang_icon");e.classList.toggle("hidden"),t.classList.toggle("mt-2")},toggleClose(){const e=document.getElementById("lang"),t=document.getElementById("lang_icon");return e.classList.add("hidden"),t.classList.toggle("mt-0"),this.openMenu=!1},open(){this.deposit=!this.deposit,document.getElementById("depo").classList.toggle("hidden")},close(){return document.getElementById("depo").classList.add("hidden"),this.deposit=!1},wdropen(){this.deposit=!this.deposit,document.getElementById("wdr").classList.toggle("hidden")},wdrclose(){return document.getElementById("wdr").classList.add("hidden"),this.deposit=!1},wopen(){this.deposit=!this.deposit;const e=document.getElementById("wdepo");document.getElementById("depo").classList.add("hidden"),e.classList.toggle("hidden")},wclose(){return document.getElementById("wdepo").classList.add("hidden"),this.deposit=!1},cookiesClose(){const e=document.getElementById("cookie");return e.classList.remove("md:flex","md:items-center"),e.classList.add("hidden","md:hidden"),this.lang=!0},wcopy(){this.copy=!this.copy;const e=document.getElementById("copy");e.select(),e.setSelectionRange(0,99999),navigator.clipboard.writeText(e.value),alert("Copied the text: "+e.value)}}})),s.Z.start(),window.Swiper=i.ZP},689:function(){window.console.log("sidebar is loaded")}},function(e){e.O(0,[812],(function(){return 262,e(e.s=262)})),e.O()}]);
//# sourceMappingURL=app.2aff501c.js.map