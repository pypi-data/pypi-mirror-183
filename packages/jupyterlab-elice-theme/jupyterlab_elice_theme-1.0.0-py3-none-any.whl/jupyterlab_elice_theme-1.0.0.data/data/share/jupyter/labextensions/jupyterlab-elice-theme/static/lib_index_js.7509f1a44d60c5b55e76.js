"use strict";
(self["webpackChunkjupyterlab_elice_theme"] = self["webpackChunkjupyterlab_elice_theme"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);

const updateFavicon = () => {
    const icons = document.getElementsByClassName('favicon');
    for (const icon of icons) {
        icon.setAttribute('href', 'https://cdn-api.elice.io/api-attachment/attachment/3c0b7e146bc6469f8b8afb928925636a/elice_project_logo.png');
    }
};
updateFavicon();
/**
 * Initialization data for the jupyterlab-elice-theme extension.
 */
const plugin = {
    id: 'jupyterlab-elice-theme:plugin',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.IThemeManager],
    activate: (app, manager) => {
        console.log('JupyterLab extension jupyterlab-elice-theme is activated!');
        const style = 'jupyterlab-elice-theme/index.css';
        manager.register({
            name: 'Elice',
            isLight: true,
            load: () => manager.loadCSS(style),
            unload: () => Promise.resolve(undefined)
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.7509f1a44d60c5b55e76.js.map