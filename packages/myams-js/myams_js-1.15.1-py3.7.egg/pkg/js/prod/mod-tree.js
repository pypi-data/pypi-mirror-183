!function(e,t){if("function"==typeof define&&define.amd)define(["exports"],t);else if("undefined"!=typeof exports)t(exports);else{var a={exports:{}};t(a.exports),e.modTree=a.exports}}("undefined"!=typeof globalThis?globalThis:"undefined"!=typeof self?self:this,(function(e){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.tree=void 0;const t=MyAMS.$,a={switchTreeNode:e=>{const a=e=>{t(`tr[data-ams-tree-node-parent-id="${e}"]`).each(((e,r)=>{const s=t(r);a(s.data("ams-tree-node-id")),n.row(s).remove().draw()}))},r=t(e.currentTarget),s=t(".switcher",r),d=r.parents("tr").first(),o=d.parents("table").first(),n=o.DataTable();if(r.tooltip("hide"),s.hasClass("expanded"))a(d.data("ams-tree-node-id")),s.html('<i class="far fa-plus-square"></i>').removeClass("expanded");else{const e=d.data("ams-location")||o.data("ams-location")||"",a=d.data("ams-tree-nodes-target")||o.data("ams-tree-nodes-target")||"get-tree-nodes.json",r=d.data("ams-element-name");s.html('<i class="fas fa-spinner fa-spin"></i>'),MyAMS.require("ajax").then((()=>{MyAMS.ajax.post(`${e}/${r}/${a}`,{can_sort:!t("td.sorter",d).is(":empty")}).then((e=>{if(e.length>0){let a;for(const r of e)a=t(r),n.row.add(a).draw(),MyAMS.core.initContent(a).then()}s.html('<i class="far fa-minus-square"></i>').addClass("expanded")}))}))}},switchTree:e=>{const a=t(e.currentTarget),r=t(".switcher",a),s=a.parents("th").parents("table").first(),d=s.data("ams-tree-node-id"),o=s.DataTable();if(a.tooltip("hide"),r.hasClass("expanded"))t("tr[data-ams-tree-node-parent-id]").filter(`tr[data-ams-tree-node-parent-id!="${d}"]`).each(((e,t)=>{o.row(t).remove().draw()})),t(".switcher",s).each(((e,a)=>{t(a).html('<i class="far fa-plus-square"></i>').removeClass("expanded")}));else{const e=s.data("ams-location")||"",a=s.data("ams-tree-nodes-target")||"get-tree.json",d=t("tbody tr",s.first());r.html('<i class="fas fa-spinner fa-spin"></i>'),MyAMS.require("ajax").then((()=>{MyAMS.ajax.post(`${e}/${a}`,{can_sort:!t("td.sorter",d).is(":empty")}).then((e=>{t("tr[data-ams-tree-node-id]",s).each(((e,t)=>{o.row(t).remove().draw()})),t(e).each(((e,a)=>{const r=t(a);o.row.add(r).draw()})),MyAMS.core.initContent(s).then(),r.html('<i class="far fa-minus-square"></i>').addClass("expanded")}))}))}},deleteElement:(e,a)=>{console.debug(a);const r=a.node_id;r&&t(`tr[data-ams-tree-node-parent-id="${r}"]`).each(((e,a)=>{t(a).parents("table").DataTable().row(a).remove().draw()}))},sortTree:(e,a)=>{const r=t(e.target),s=r.DataTable(),d=t(r).data();let o=d.amsReorderUrl;if(o){const e=t(d.amsReorderSource.node);e.data("ams-disabled-handlers","click");try{const a=e.parents("table").first().data("ams-tree-node-id"),n=e.data("ams-tree-node-id"),i=e.data("ams-tree-node-parent-id"),l=e.prev("tr");let c,m,f;l.exists()?(c=l.data("ams-tree-node-id"),m=t(".switch",l),m.hasClass("minus")||(c=l.data("ams-tree-node-parent-id")),f=i===c?"reorder":"reparent"):(c=a,m=null,f=i===c?"reorder":"reparent");const p=MyAMS.core.getFunctionByName(o);if("function"==typeof p)p.call(r,dnd_table,post_data);else{if(!o.startsWith(window.location.protocol)){const e=d.amsLocation;e&&(o=`${e}/${o}`)}const a={action:f,child:n,parent:c,order:JSON.stringify(t("tr[data-ams-tree-node-id]").listattr("data-ams-tree-node-id")),can_sort:!t("td.sorter",e).is(":empty")};MyAMS.require("ajax").then((()=>{MyAMS.ajax.post(o,a).then((r=>{const d=e=>{t(`tr[data-ams-tree-node-parent-id="${e}"]`).each(((e,a)=>{const r=t(a),o=r.attr("data-ams-tree-node-id");d(o),s.row(r).remove().draw()}))};if(r.status)MyAMS.ajax.handleJSON(r);else{let o,i;"reparent"===a.action&&(e=>{const a=t(`tr[data-ams-tree-node-id="${e}"]`);s.row(a).remove().draw()})(c),d(c),d(n),s.row(e).remove().draw();for(const e of r)o=t(e),i=t(`tr[id="${o.attr("id")}"]`),s.row(i).remove().draw(),s.row.add(o).draw(),MyAMS.core.initContent(o).then()}}))}))}}finally{setTimeout((function(){t(e).removeData("ams-disabled-handlers")}),50)}}return!1}};e.tree=a,window.MyAMS&&(MyAMS.env.bundle?MyAMS.config.modules.push("tree"):(MyAMS.tree=a,console.debug("MyAMS: tree module loaded...")))}));