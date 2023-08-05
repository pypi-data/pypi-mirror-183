/**
 * Copyright (c) Tiny Technologies, Inc. All rights reserved.
 * Licensed under the LGPL or a commercial license.
 * For LGPL see License.txt in the project root for license information.
 * For commercial licenses see https://www.tiny.cloud/
 *
 * Version: 5.6.2 (2020-12-08)
 */
!function(){"use strict";var e=tinymce.util.Tools.resolve("tinymce.PluginManager"),l=tinymce.util.Tools.resolve("tinymce.util.Tools"),t=function(s){var e,t,i,a;t=!1,(e=s).settings.inline_styles=t,e.getParam("fontsize_formats")||(i="8pt=1 10pt=2 12pt=3 14pt=4 18pt=5 24pt=6 36pt=7",e.settings.fontsize_formats=i),e.getParam("font_formats")||(a="Andale Mono=andale mono,monospace;Arial=arial,helvetica,sans-serif;Arial Black=arial black,sans-serif;Book Antiqua=book antiqua,palatino,serif;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier,monospace;Georgia=georgia,palatino,serif;Helvetica=helvetica,arial,sans-serif;Impact=impact,sans-serif;Symbol=symbol;Tahoma=tahoma,arial,helvetica,sans-serif;Terminal=terminal,monaco,monospace;Times New Roman=times new roman,times,serif;Trebuchet MS=trebuchet ms,geneva,sans-serif;Verdana=verdana,geneva,sans-serif;Webdings=webdings;Wingdings=wingdings,zapf dingbats",e.settings.font_formats=a),s.on("PreInit",function(){return e=s,t="p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table",i=l.explode(e.getParam("font_size_style_values","xx-small,x-small,small,medium,large,x-large,xx-large")),a=e.schema,e.formatter.register({alignleft:{selector:t,attributes:{align:"left"}},aligncenter:{selector:t,attributes:{align:"center"}},alignright:{selector:t,attributes:{align:"right"}},alignjustify:{selector:t,attributes:{align:"justify"}},bold:[{inline:"b",remove:"all",preserve_attributes:["class","style"]},{inline:"strong",remove:"all",preserve_attributes:["class","style"]},{inline:"span",styles:{fontWeight:"bold"}}],italic:[{inline:"i",remove:"all",preserve_attributes:["class","style"]},{inline:"em",remove:"all",preserve_attributes:["class","style"]},{inline:"span",styles:{fontStyle:"italic"}}],underline:[{inline:"u",remove:"all",preserve_attributes:["class","style"]},{inline:"span",styles:{textDecoration:"underline"},exact:!0}],strikethrough:[{inline:"strike",remove:"all",preserve_attributes:["class","style"]},{inline:"span",styles:{textDecoration:"line-through"},exact:!0}],fontname:{inline:"font",toggle:!1,attributes:{face:"%value"}},fontsize:{inline:"font",toggle:!1,attributes:{size:function(e){return String(l.inArray(i,e.value)+1)}}},forecolor:{inline:"font",attributes:{color:"%value"},links:!0,remove_similar:!0,clear_child_styles:!0},hilitecolor:{inline:"font",styles:{backgroundColor:"%value"},links:!0,remove_similar:!0,clear_child_styles:!0}}),l.each("b,i,u,strike".split(","),function(e){a.addValidElements(e+"[*]")}),a.getElementRule("font")||a.addValidElements("font[face|size|color|style]"),void l.each(t.split(","),function(e){var t=a.getElementRule(e);t&&(t.attributes.align||(t.attributes.align={},t.attributesOrder.push("align")))});var e,t,i,a})};e.add("legacyoutput",function(e){t(e)})}();