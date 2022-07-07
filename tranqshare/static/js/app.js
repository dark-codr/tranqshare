(self["webpackChunkpython_webpack_boilerplate"] = self["webpackChunkpython_webpack_boilerplate"] || []).push([["app"],{

/***/ "./frontend/src/application/app.js":
/*!*****************************************!*\
  !*** ./frontend/src/application/app.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _styles_index_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../styles/index.scss */ "./frontend/src/styles/index.scss");
/* harmony import */ var htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! htmx.org/dist/htmx */ "./node_modules/htmx.org/dist/htmx.js");
/* harmony import */ var htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var alpinejs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! alpinejs */ "./node_modules/alpinejs/dist/module.esm.js");
/* harmony import */ var swiper__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! swiper */ "./node_modules/swiper/swiper.esm.js");
/* harmony import */ var _components_sidebar__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../components/sidebar */ "./frontend/src/components/sidebar.js");
/* harmony import */ var _components_sidebar__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_components_sidebar__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _components_drop_lang_js__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../components/drop_lang.js */ "./frontend/src/components/drop_lang.js");
// This is the scss entry file



 // We can import other JS file as we like


 // import axios from '../components/axiosFactory';
// import { detect } from 'detect-browser';

window.htmx = (htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default()); // const browser = detect();

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
});
window.Alpine = alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"];
alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].data('lang_drop', _components_drop_lang_js__WEBPACK_IMPORTED_MODULE_5__["default"]); // Alpine.data('playlistToggle', playlistToggle);

alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].start();
window.Swiper = swiper__WEBPACK_IMPORTED_MODULE_3__["default"];

if (true) {
  // enable logging for htmx in development server
  window.htmx.logAll();
}

/***/ }),

/***/ "./frontend/src/components/drop_lang.js":
/*!**********************************************!*\
  !*** ./frontend/src/components/drop_lang.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ langDropdownMenu)
/* harmony export */ });
function langDropdownMenu() {
  return {
    openMenu: false,
    deposit: false,
    lang: false,
    copy: false,

    toggleOpen() {
      this.openMenu = !this.openMenu;
      const menu = document.getElementById("lang");
      const icon = document.getElementById("lang_icon");
      menu.classList.toggle("hidden");
      icon.classList.toggle("mt-2");
    },

    toggleClose() {
      const menu = document.getElementById("lang");
      const icon = document.getElementById("lang_icon");
      menu.classList.add("hidden");
      icon.classList.toggle("mt-0");
      return this.openMenu = false;
    },

    open() {
      this.deposit = !this.deposit;
      const menu = document.getElementById("depo");
      menu.classList.toggle("hidden");
    },

    close() {
      const menu = document.getElementById("depo");
      menu.classList.add("hidden");
      return this.deposit = false;
    },

    wdropen() {
      this.deposit = !this.deposit;
      const menu = document.getElementById("wdr");
      menu.classList.toggle("hidden");
    },

    wdrclose() {
      const menu = document.getElementById("wdr");
      menu.classList.add("hidden");
      return this.deposit = false;
    },

    wopen() {
      this.deposit = !this.deposit;
      const menu = document.getElementById("wdepo");
      const old = document.getElementById("depo");
      old.classList.add("hidden");
      menu.classList.toggle("hidden");
    },

    wclose() {
      const menu = document.getElementById("wdepo");
      menu.classList.add("hidden");
      return this.deposit = false;
    },

    cookiesClose() {
      const cookie = document.getElementById("cookie");
      cookie.classList.remove("md:flex", "md:items-center");
      cookie.classList.add("hidden", "md:hidden");
      return this.lang = true;
    },

    wcopy() {
      this.copy = !this.copy;
      const menu = document.getElementById("copy");
      menu.select();
      menu.setSelectionRange(0, 99999);
      navigator.clipboard.writeText(menu.value);
      alert("Copied the text: " + menu.value);
    }

  };
}

/***/ }),

/***/ "./frontend/src/components/sidebar.js":
/*!********************************************!*\
  !*** ./frontend/src/components/sidebar.js ***!
  \********************************************/
/***/ (() => {

window.console.log("sidebar is loaded");

/***/ }),

/***/ "./frontend/src/styles/index.scss":
/*!****************************************!*\
  !*** ./frontend/src/styles/index.scss ***!
  \****************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin

    if(true) {
      // 1657204222535
      var cssReload = __webpack_require__(/*! ../../../node_modules/mini-css-extract-plugin/dist/hmr/hotModuleReplacement.js */ "./node_modules/mini-css-extract-plugin/dist/hmr/hotModuleReplacement.js")(module.id, {"locals":false});
      module.hot.dispose(cssReload);
      module.hot.accept(undefined, cssReload);
    }
  

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ __webpack_require__.O(0, ["vendors-node_modules_webpack-dev-server_client_index_js_protocol_ws_3A_hostname_0_0_0_0_port_-0bf9f2","vendors-node_modules_alpinejs_dist_module_esm_js-node_modules_htmx_org_dist_htmx_js-node_modu-17a218"], () => (__webpack_exec__("./node_modules/webpack-dev-server/client/index.js?protocol=ws%3A&hostname=0.0.0.0&port=9091&pathname=%2Fws&logging=info&reconnect=10"), __webpack_exec__("./node_modules/webpack/hot/dev-server.js"), __webpack_exec__("./frontend/src/application/app.js")));
/******/ var __webpack_exports__ = __webpack_require__.O();
/******/ }
]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,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QyxLQUFLLENBQUMsc0JBQXNCeEIsSUFBSSxDQUFDdUIsS0FBNUIsQ0FBTDtJQUNIOztFQTFFRSxDQUFQO0FBOEVIOzs7Ozs7Ozs7O0FDL0VEdkMsTUFBTSxDQUFDRyxPQUFQLENBQWVDLEdBQWYsQ0FBbUIsbUJBQW5COzs7Ozs7Ozs7Ozs7QUNBQTtBQUNVO0FBQ1YsT0FBTyxJQUFVO0FBQ2pCO0FBQ0Esc0JBQXNCLG1CQUFPLENBQUMsK0pBQWdGLGNBQWMsZUFBZTtBQUMzSSxNQUFNLFVBQVU7QUFDaEIsTUFBTSxpQkFBaUI7QUFDdkI7QUFDQSIsInNvdXJjZXMiOlsid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vZnJvbnRlbmQvc3JjL2FwcGxpY2F0aW9uL2FwcC5qcyIsIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL2Zyb250ZW5kL3NyYy9jb21wb25lbnRzL2Ryb3BfbGFuZy5qcyIsIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL2Zyb250ZW5kL3NyYy9jb21wb25lbnRzL3NpZGViYXIuanMiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9mcm9udGVuZC9zcmMvc3R5bGVzL2luZGV4LnNjc3MiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gVGhpcyBpcyB0aGUgc2NzcyBlbnRyeSBmaWxlXG5pbXBvcnQgXCIuLi9zdHlsZXMvaW5kZXguc2Nzc1wiO1xuaW1wb3J0IGh0bXggZnJvbSAnaHRteC5vcmcvZGlzdC9odG14JztcbmltcG9ydCBBbHBpbmUgZnJvbSAnYWxwaW5lanMnO1xuaW1wb3J0IFN3aXBlciBmcm9tICdzd2lwZXInO1xuXG4vLyBXZSBjYW4gaW1wb3J0IG90aGVyIEpTIGZpbGUgYXMgd2UgbGlrZVxuaW1wb3J0IFwiLi4vY29tcG9uZW50cy9zaWRlYmFyXCI7XG5pbXBvcnQgbGFuZ0Ryb3Bkb3duTWVudSBmcm9tIFwiLi4vY29tcG9uZW50cy9kcm9wX2xhbmcuanNcIjtcbi8vIGltcG9ydCBheGlvcyBmcm9tICcuLi9jb21wb25lbnRzL2F4aW9zRmFjdG9yeSc7XG4vLyBpbXBvcnQgeyBkZXRlY3QgfSBmcm9tICdkZXRlY3QtYnJvd3Nlcic7XG5cbndpbmRvdy5odG14ID0gaHRteDtcbi8vIGNvbnN0IGJyb3dzZXIgPSBkZXRlY3QoKTtcblxud2luZG93LmRvY3VtZW50LmFkZEV2ZW50TGlzdGVuZXIoXCJET01Db250ZW50TG9hZGVkXCIsIGZ1bmN0aW9uICgpIHtcbiAgd2luZG93LmNvbnNvbGUubG9nKFwiZG9tIHJlYWR5IDFcIik7XG59KTtcbndpbmRvdy5BbHBpbmUgPSBBbHBpbmU7XG5BbHBpbmUuZGF0YSgnbGFuZ19kcm9wJywgbGFuZ0Ryb3Bkb3duTWVudSk7XG4vLyBBbHBpbmUuZGF0YSgncGxheWxpc3RUb2dnbGUnLCBwbGF5bGlzdFRvZ2dsZSk7XG5BbHBpbmUuc3RhcnQoKTtcblxud2luZG93LlN3aXBlciA9IFN3aXBlcjtcbmlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gJ2RldmVsb3BtZW50Jykge1xuICAvLyBlbmFibGUgbG9nZ2luZyBmb3IgaHRteCBpbiBkZXZlbG9wbWVudCBzZXJ2ZXJcbiAgd2luZG93Lmh0bXgubG9nQWxsKCk7XG59XG5cbiIsImV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIGxhbmdEcm9wZG93bk1lbnUoKSB7XG4gICAgcmV0dXJuIHtcbiAgICAgICAgb3Blbk1lbnU6IGZhbHNlLFxuICAgICAgICBkZXBvc2l0OiBmYWxzZSxcbiAgICAgICAgbGFuZzogZmFsc2UsXG4gICAgICAgIGNvcHk6IGZhbHNlLFxuXG4gICAgICAgIHRvZ2dsZU9wZW4oKSB7XG4gICAgICAgICAgICB0aGlzLm9wZW5NZW51ID0gIXRoaXMub3Blbk1lbnU7XG4gICAgICAgICAgICBjb25zdCBtZW51ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJsYW5nXCIpO1xuICAgICAgICAgICAgY29uc3QgaWNvbiA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwibGFuZ19pY29uXCIpO1xuICAgICAgICAgICAgbWVudS5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIpO1xuICAgICAgICAgICAgaWNvbi5jbGFzc0xpc3QudG9nZ2xlKFwibXQtMlwiKTtcbiAgICAgICAgfSxcblxuICAgICAgICB0b2dnbGVDbG9zZSgpIHtcbiAgICAgICAgICAgIGNvbnN0IG1lbnUgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImxhbmdcIik7XG4gICAgICAgICAgICBjb25zdCBpY29uID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJsYW5nX2ljb25cIik7XG4gICAgICAgICAgICBtZW51LmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XG4gICAgICAgICAgICBpY29uLmNsYXNzTGlzdC50b2dnbGUoXCJtdC0wXCIpO1xuICAgICAgICAgICAgcmV0dXJuIHRoaXMub3Blbk1lbnUgPSBmYWxzZTtcbiAgICAgICAgfSxcblxuICAgICAgICBvcGVuKCkge1xuICAgICAgICAgICAgdGhpcy5kZXBvc2l0ID0gIXRoaXMuZGVwb3NpdDtcbiAgICAgICAgICAgIGNvbnN0IG1lbnUgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImRlcG9cIik7XG4gICAgICAgICAgICBtZW51LmNsYXNzTGlzdC50b2dnbGUoXCJoaWRkZW5cIik7XG4gICAgICAgIH0sXG5cbiAgICAgICAgY2xvc2UoKSB7XG4gICAgICAgICAgICBjb25zdCBtZW51ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJkZXBvXCIpO1xuICAgICAgICAgICAgbWVudS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xuICAgICAgICAgICAgcmV0dXJuIHRoaXMuZGVwb3NpdCA9IGZhbHNlO1xuICAgICAgICB9LFxuXG4gICAgICAgIHdkcm9wZW4oKSB7XG4gICAgICAgICAgICB0aGlzLmRlcG9zaXQgPSAhdGhpcy5kZXBvc2l0O1xuICAgICAgICAgICAgY29uc3QgbWVudSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwid2RyXCIpO1xuICAgICAgICAgICAgbWVudS5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIpO1xuICAgICAgICB9LFxuXG4gICAgICAgIHdkcmNsb3NlKCkge1xuICAgICAgICAgICAgY29uc3QgbWVudSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwid2RyXCIpO1xuICAgICAgICAgICAgbWVudS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xuICAgICAgICAgICAgcmV0dXJuIHRoaXMuZGVwb3NpdCA9IGZhbHNlO1xuICAgICAgICB9LFxuXG4gICAgICAgIHdvcGVuKCkge1xuICAgICAgICAgICAgdGhpcy5kZXBvc2l0ID0gIXRoaXMuZGVwb3NpdDtcbiAgICAgICAgICAgIGNvbnN0IG1lbnUgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcIndkZXBvXCIpO1xuICAgICAgICAgICAgY29uc3Qgb2xkID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJkZXBvXCIpO1xuICAgICAgICAgICAgb2xkLmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XG4gICAgICAgICAgICBtZW51LmNsYXNzTGlzdC50b2dnbGUoXCJoaWRkZW5cIik7XG4gICAgICAgIH0sXG5cbiAgICAgICAgd2Nsb3NlKCkge1xuICAgICAgICAgICAgY29uc3QgbWVudSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwid2RlcG9cIik7XG4gICAgICAgICAgICBtZW51LmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XG4gICAgICAgICAgICByZXR1cm4gdGhpcy5kZXBvc2l0ID0gZmFsc2U7XG4gICAgICAgIH0sXG5cbiAgICAgICAgY29va2llc0Nsb3NlKCkge1xuICAgICAgICAgICAgY29uc3QgY29va2llID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJjb29raWVcIik7XG4gICAgICAgICAgICBjb29raWUuY2xhc3NMaXN0LnJlbW92ZShcIm1kOmZsZXhcIiwgXCJtZDppdGVtcy1jZW50ZXJcIik7XG4gICAgICAgICAgICBjb29raWUuY2xhc3NMaXN0LmFkZChcImhpZGRlblwiLCBcIm1kOmhpZGRlblwiKTtcbiAgICAgICAgICAgIHJldHVybiB0aGlzLmxhbmcgPSB0cnVlO1xuICAgICAgICB9LFxuXG4gICAgICAgIHdjb3B5KCkge1xuICAgICAgICAgICAgdGhpcy5jb3B5ID0gIXRoaXMuY29weTtcbiAgICAgICAgICAgIGNvbnN0IG1lbnUgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImNvcHlcIik7XG4gICAgICAgICAgICBtZW51LnNlbGVjdCgpO1xuICAgICAgICAgICAgbWVudS5zZXRTZWxlY3Rpb25SYW5nZSgwLCA5OTk5OSk7XG4gICAgICAgICAgICBuYXZpZ2F0b3IuY2xpcGJvYXJkLndyaXRlVGV4dChtZW51LnZhbHVlKTtcbiAgICAgICAgICAgIGFsZXJ0KFwiQ29waWVkIHRoZSB0ZXh0OiBcIiArIG1lbnUudmFsdWUpO1xuICAgICAgICB9XG5cblxuICAgIH07XG59XG4iLCJ3aW5kb3cuY29uc29sZS5sb2coXCJzaWRlYmFyIGlzIGxvYWRlZFwiKTtcbiIsIi8vIGV4dHJhY3RlZCBieSBtaW5pLWNzcy1leHRyYWN0LXBsdWdpblxuZXhwb3J0IHt9O1xuICAgIGlmKG1vZHVsZS5ob3QpIHtcbiAgICAgIC8vIDE2NTcyMDQyMjI1MzVcbiAgICAgIHZhciBjc3NSZWxvYWQgPSByZXF1aXJlKFwiLi4vLi4vLi4vbm9kZV9tb2R1bGVzL21pbmktY3NzLWV4dHJhY3QtcGx1Z2luL2Rpc3QvaG1yL2hvdE1vZHVsZVJlcGxhY2VtZW50LmpzXCIpKG1vZHVsZS5pZCwge1wibG9jYWxzXCI6ZmFsc2V9KTtcbiAgICAgIG1vZHVsZS5ob3QuZGlzcG9zZShjc3NSZWxvYWQpO1xuICAgICAgbW9kdWxlLmhvdC5hY2NlcHQodW5kZWZpbmVkLCBjc3NSZWxvYWQpO1xuICAgIH1cbiAgIl0sIm5hbWVzIjpbImh0bXgiLCJBbHBpbmUiLCJTd2lwZXIiLCJsYW5nRHJvcGRvd25NZW51Iiwid2luZG93IiwiZG9jdW1lbnQiLCJhZGRFdmVudExpc3RlbmVyIiwiY29uc29sZSIsImxvZyIsImRhdGEiLCJzdGFydCIsInByb2Nlc3MiLCJlbnYiLCJOT0RFX0VOViIsImxvZ0FsbCIsIm9wZW5NZW51IiwiZGVwb3NpdCIsImxhbmciLCJjb3B5IiwidG9nZ2xlT3BlbiIsIm1lbnUiLCJnZXRFbGVtZW50QnlJZCIsImljb24iLCJjbGFzc0xpc3QiLCJ0b2dnbGUiLCJ0b2dnbGVDbG9zZSIsImFkZCIsIm9wZW4iLCJjbG9zZSIsIndkcm9wZW4iLCJ3ZHJjbG9zZSIsIndvcGVuIiwib2xkIiwid2Nsb3NlIiwiY29va2llc0Nsb3NlIiwiY29va2llIiwicmVtb3ZlIiwid2NvcHkiLCJzZWxlY3QiLCJzZXRTZWxlY3Rpb25SYW5nZSIsIm5hdmlnYXRvciIsImNsaXBib2FyZCIsIndyaXRlVGV4dCIsInZhbHVlIiwiYWxlcnQiXSwic291cmNlUm9vdCI6IiJ9