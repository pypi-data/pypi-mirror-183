!function(e,t){if("function"==typeof define&&define.amd)define(["exports"],t);else if("undefined"!=typeof exports)t(exports);else{var o={exports:{}};t(o.exports),e.modStats=o.exports}}("undefined"!=typeof globalThis?globalThis:"undefined"!=typeof self?self:this,(function(e){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.stats=void 0;MyAMS.$;const t={logPageview:function(){},logEvent:function(){}};e.stats=t,window.MyAMS&&(MyAMS.env.bundle?MyAMS.config.modules.push("stats"):(MyAMS.stats=t,console.debug("MyAMS: stats module loaded...")))}));