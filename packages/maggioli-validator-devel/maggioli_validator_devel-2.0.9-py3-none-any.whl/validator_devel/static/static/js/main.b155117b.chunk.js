(this["webpackJsonpvalidator-react"]=this["webpackJsonpvalidator-react"]||[]).push([[0],{165:function(e,t,n){e.exports=n(400)},174:function(e,t,n){},391:function(e,t,n){},400:function(e,t,n){"use strict";n.r(t);var r=n(0),a=n.n(r),o=n(25),c=n.n(o),l=n(16),s=n(31),u=n(164),i=n(37),d="SET_QUERY_FILTER",p="CHANGED_QUERY_FILTER",E="SET_FIELD_FILTER",f="MODULE_DATA_REQUEST",m="MODULE_DATA_RECEIVED",b="MODULE_DATA_ERROR";function O(e){return{type:p,query:e}}function h(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function y(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?h(Object(n),!0).forEach((function(t){Object(i.a)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):h(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var g="FIELD_PATH";var j=Object(s.c)({fieldFilter:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:g,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case E:return t.field;default:return e}},queryFilter:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments.length>1?arguments[1]:void 0;switch(t.type){case d:return t.query;default:return e}},modules:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1?arguments[1]:void 0;switch(t.type){case f:return e;case m:return t.modules;default:return e}},currentDownloadStatus:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{module:null,folders:null,lastError:null},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"PREPARE_FOLDER_REQUEST":case"PREPARE_MODULE_REQUEST":case"PREPARE_PDF_REQUEST":return t.hasOwnProperty("folders")?y({},e,{folders:t.folders,lastError:null}):t.hasOwnProperty("module_key")?y({},e,{module:t.module_key,lastError:null}):e;case"PREPARE_FOLDER_ERROR":case"PREPARE_MODULE_ERROR":case"PREPARE_FOLDER_REQUEST_ERROR":case"PREPARE_MODULE_REQUEST_ERROR":case"PREPARE_PDF_REQUEST_ERROR":return{lastError:t.error,module:null,folders:null};case"PREPARE_FOLDER_RECEIVED":case"PREPARE_MODULE_RECEIVED":case"PREPARE_PDF_RECEIVED":return{lastError:null,module:null,folders:null};case"CLEAN_ERROR":return y({},e,{lastError:null});default:return e}},settings:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{stu3Flag:!1},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"UPDATE_SETTING":return y({},e,{},t.settings);default:return e}}}),R=(n(174),n(26)),v=n(27),_=n(29),w=n(28),P=n(30),k=n(23),D=n(96),x=n.n(D),A=n(46),S=n.n(A),C=n(78),T=n.n(C),L=n(143),U=n.n(L),F=n(74),I=n.n(F),N=n(75),M=n.n(N),Q=n(76),q=n.n(Q),W=n(39),B=n.n(W),V=n(144),z=n.n(V),Y=n(22),G=n.n(Y),H=n(145),J=n.n(H),X=n(77),$=n.n(X),K=n(148),Z=n.n(K),ee=n(146),te=n.n(ee),ne=n(147),re=n.n(ne);var ae=Object(k.withStyles)((function(e){return{noMaxWidth:{maxWidth:"none"},folderContainer:{justifyContent:"center",alignItems:"flex-end"},folderIcon:{margin:0,verticalAlign:"middle",color:"#969696",marginRight:.5*e.spacing.unit}}}))(Object(l.b)((function(e,t){var n=U()(e.modules,(function(e){return e.key===t.moduleId}));if(n<0)throw new Error("Can't find module with ID: ".concat(t.moduleId," in the store."));return{module:e.modules[n],working:!!e.currentDownloadStatus.module||!!e.currentDownloadStatus.folders}}))((function(e){var t=e.classes,n=e.module,r=e.dispatch,o=e.working,c=Object(l.d)((function(e){return e.settings.stu3Flag}))?"?stu3=true":"";return a.a.createElement(I.a,{divider:!0,button:!0,onClick:function(){return window.open("/module/".concat(n.key).concat(c),"_blank")}},a.a.createElement(M.a,null,a.a.createElement(z.a,{title:n.file_path,placement:"left",classes:{tooltip:t.noMaxWidth}},a.a.createElement(J.a,null))),a.a.createElement(q.a,{primary:a.a.createElement(a.a.Fragment,null,a.a.createElement("div",{className:t.folderContainer},a.a.createElement(te.a,{className:t.folderIcon,fontSize:"small"}),n.folders.join("/"))),secondary:a.a.createElement(a.a.Fragment,null,a.a.createElement(G.a,{component:"span",className:t.inline,color:"textPrimary"},n.filename),n.urn)}),a.a.createElement(B.a,{disabled:o,onClick:function(e){e.stopPropagation(),r({type:"EDIT_MODULE_REQUEST",module_key:n.key}),console.log("Edit module with key: ".concat(n.key))}},a.a.createElement(re.a,null)),a.a.createElement(B.a,{disabled:o,onClick:function(e){e.stopPropagation(),r({type:"PREPARE_MODULE_REQUEST",module_key:n.key}),console.log("Download module with key: ".concat(n.key))}},a.a.createElement($.a,null)),a.a.createElement(B.a,{disabled:o,onClick:function(e){e.stopPropagation(),r({type:"PREPARE_PDF_REQUEST",module_key:n.key}),console.log("Download PDF for module with key: ".concat(n.key))}},a.a.createElement(Z.a,null)))})));function oe(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function ce(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?oe(Object(n),!0).forEach((function(t){Object(i.a)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):oe(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var le=function(e){function t(){return Object(R.a)(this,t),Object(_.a)(this,Object(w.a)(t).apply(this,arguments))}return Object(P.a)(t,e),Object(v.a)(t,[{key:"render",value:function(){var e=this.props,t=e.classes,n=e.modules;return Array.isArray(n)?a.a.createElement(S.a,{className:t.search_result,elevation:1},a.a.createElement(T.a,{dense:!0,component:"nav"},n.map((function(e){return a.a.createElement(ae,{moduleId:e,key:e})})))):a.a.createElement("div",null)}}]),t}(a.a.Component),se=Object(k.withStyles)((function(e){return{search_result:ce({},e.mixins.gutters(),{paddingTop:2*e.spacing.unit,paddingBottom:2*e.spacing.unit,marginLeft:8*e.spacing.unit,marginRight:8*e.spacing.unit}),noMaxWidth:{maxWidth:"none"}}}))(le),ue=n(149),ie=n.n(ue),de=function(e,t){if(""===t)return{};return ie.a.go(t,e,{limit:30,threshold:-1e4,keys:["file_path","folders_search","urn","code"]}).map((function(e){return e.obj.key}))},pe=Object(l.b)((function(e){return{modules:de(e.modules,e.queryFilter)}}),(function(e){return{onSearchCange:function(t){e(O(t))}}}))(se),Ee=n(150),fe=n.n(Ee),me=n(155),be=n.n(me),Oe=n(152),he=n.n(Oe),ye=n(151),ge=n.n(ye),je=n(153),Re=n.n(je),ve=n(154),_e=n.n(ve),we=n(80);function Pe(e,t){return Object(we.a)(new Set(e.filter((function(e){return e.folders_search.startsWith(t.join("/"))})).filter((function(e){return e.folders.length>t.length})).map((function(e){return e.folders[t.length]})).sort()))}var ke=function(e){function t(){return Object(R.a)(this,t),Object(_.a)(this,Object(w.a)(t).apply(this,arguments))}return Object(P.a)(t,e),Object(v.a)(t,[{key:"render",value:function(){var e=this.props,t=e.subModules,n=e.subFolders,r=e.folders,o=n.map((function(e){return a.a.createElement(Ce,{key:[].concat(Object(we.a)(r),[e]).join("/"),folders:[].concat(Object(we.a)(r),[e])})})),c=t.map((function(e){return a.a.createElement(ae,{moduleId:e.key,key:e.key})}));return a.a.createElement(T.a,{dense:!0,component:"div",style:{paddingLeft:16*r.length}},o,c)}}]),t}(a.a.Component),De=Object(l.b)((function(e,t){return{subModules:(n=e.modules,r=t.folders,n.filter((function(e){return e.folders_search===r.join("/")})).sort()),subFolders:Pe(e.modules,t.folders)};var n,r}))(ke);function xe(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function Ae(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?xe(Object(n),!0).forEach((function(t){Object(i.a)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):xe(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var Se=function(e){return{search_result:Ae({},e.mixins.gutters(),{paddingTop:2*e.spacing.unit,paddingBottom:2*e.spacing.unit,marginLeft:8*e.spacing.unit,marginRight:8*e.spacing.unit}),progress:{position:"absolute",top:0,left:0,zIndex:1}}},Ce=function(e){function t(e){var n;return Object(R.a)(this,t),(n=Object(_.a)(this,Object(w.a)(t).call(this,e))).toogleOpen=function(){n.setState((function(e){return{open:!e.open}}))},n.state={open:!1},n}return Object(P.a)(t,e),Object(v.a)(t,[{key:"render",value:function(){var e=this.props,t=e.classes,n=e.downloadLoading,r=e.folders,o=e.dispatch;return a.a.createElement("div",null,a.a.createElement(I.a,{divider:!0,button:!0,onClick:this.toogleOpen},a.a.createElement(M.a,null,a.a.createElement(ge.a,null)),a.a.createElement(q.a,{inset:!0,primary:r[r.length-1]}),a.a.createElement(B.a,{disabled:n,onClick:function(e){e.stopPropagation(),o(function(e){return{type:"PREPARE_FOLDER_REQUEST",folders:e}}(r))}},a.a.createElement($.a,null),n&&a.a.createElement(he.a,{size:50,className:t.progress})),this.state.open?a.a.createElement(Re.a,null):a.a.createElement(_e.a,null)),a.a.createElement(be.a,{in:this.state.open,timeout:"auto",unmountOnExit:!0},a.a.createElement(De,{folders:r})))}}]),t}(a.a.Component),Te=function(e){function t(){return Object(R.a)(this,t),Object(_.a)(this,Object(w.a)(t).apply(this,arguments))}return Object(P.a)(t,e),Object(v.a)(t,[{key:"render",value:function(){var e=this.props,t=e.classes,n=e.modules;return Array.isArray(n)?a.a.createElement(S.a,{className:t.search_result,elevation:1},a.a.createElement(De,{folders:[]})):a.a.createElement(S.a,{className:t.search_result,elevation:1},a.a.createElement(G.a,{variant:"h5"},"No modules."))}}]),t}(a.a.Component);Te=Object(k.withStyles)(Se)(Te),Ce=Object(k.withStyles)(Se)(Object(l.b)((function(e,t){return e.currentDownloadStatus.hasOwnProperty("folders")&&Array.isArray(e.currentDownloadStatus.folders)&&fe()(e.currentDownloadStatus.folders.join("/"),t.folders.join("/"))?{downloadLoading:!0}:{downloadLoading:!1}}))(Ce));var Le=Object(l.b)((function(e){return{modules:e.modules}}),(function(e){return{}}))(Te),Ue=n(159),Fe=n.n(Ue),Ie=n(160),Ne=n.n(Ie),Me=n(158),Qe=n.n(Me),qe=n(161),We=n.n(qe),Be=n(157),Ve=n.n(Be),ze=n(156),Ye=n.n(ze);function Ge(){var e=Object(l.c)(),t=Object(l.d)((function(e){return e.settings.stu3Flag}));return a.a.createElement(Ye.a,{control:a.a.createElement(Ve.a,{checked:t,onChange:function(t){return e({type:"UPDATE_SETTING",settings:{stu3Flag:t.target.checked}})},value:"stu3_flag",color:"primary"}),label:"STU3 loader"})}var He=Object(k.withStyles)((function(e){return{search_box:{marginTop:4*e.spacing.unit,marginBottom:4*e.spacing.unit,width:"100%"}}}))(Object(l.b)()((function(e){var t=e.dispatch,n=e.classes;return a.a.createElement(Qe.a,{className:n.search_box},a.a.createElement(Fe.a,{id:"search-input",startAdornment:a.a.createElement(Ne.a,{position:"start"},a.a.createElement(We.a,null)),onChange:function(e){e.preventDefault(),t(O(e.target.value))}}),a.a.createElement(Ge,null))}))),Je=n(97),Xe=n(163),$e=n.n(Xe),Ke=n(162),Ze=n.n(Ke),et=n(79),tt=n.n(et),nt=function(e){function t(){var e,n;Object(R.a)(this,t);for(var r=arguments.length,o=new Array(r),c=0;c<r;c++)o[c]=arguments[c];return(n=Object(_.a)(this,(e=Object(w.a)(t)).call.apply(e,[this].concat(o)))).state={open:!1},n.handleClose=function(){(0,n.props.dispatch)({type:"CLEAN_ERROR"})},n.errorHeaderMessage=function(){var e=n.props.error;if(null==e)return a.a.createElement("div",null,"No error to display.");var t=e.type.split("."),r=Object(Je.a)(t,2),o=r[0],c=r[1];switch(console.log("CANI CANI CANI",e,o,c),o){case"folder_request":return a.a.createElement(G.a,{variant:"body1"},"La generazione della cartella ",a.a.createElement("em",null,e.request)," \xe8 fallita");case"module_request":return a.a.createElement(G.a,{variant:"body1"},"La generazione del modulo ",a.a.createElement("em",null,e.request)," \xe8 fallita");default:return}},n.errorContentMessage=function(){var e=n.props.error;if(null==e)return a.a.createElement("div",null,"No error to display.");var t=e.type.split("."),r=Object(Je.a)(t,2),o=r[0],c=r[1];switch(console.log("CANI CANI CANI",e,o,c),c){case"key_error":return a.a.createElement(G.a,{variant:"body1"},"Non \xe8 stato trovato un modulo con questo URN: ",a.a.createElement("em",null,e.missing_key));case"template_not_found":return a.a.createElement("div",null,a.a.createElement(G.a,{variant:"body1"},"Non sono stati trovati template con questi nomi:"),a.a.createElement("ul",null,e.missing_templates.map((function(e){return a.a.createElement("li",null,e)}))),a.a.createElement(G.a,{variant:"body1"},"In genere sono nella prozione ",a.a.createElement("em",null,"extends")," del modulo."));default:return}},n}return Object(P.a)(t,e),Object(v.a)(t,[{key:"render",value:function(){var e=this.props,t=e.error,n=e.classes;return a.a.createElement("div",null,a.a.createElement(Ze.a,{onClose:this.handleClose,"aria-labelledby":"error-dialog",open:null!=t},a.a.createElement(G.a,{variant:"h4",className:n.dialogContent},"La generazione del modulo \xe8 fallita"),a.a.createElement(tt.a,{variant:"middle"}),a.a.createElement("div",{className:n.dialogContent},this.errorHeaderMessage(),this.errorContentMessage()),a.a.createElement(G.a,{variant:"body1"}),a.a.createElement(tt.a,{variant:"middle"}),a.a.createElement("pre",{fontFamily:"Monospace",m:1,className:n.dialogContent},t&&t.stacktrace.join("\n")),a.a.createElement(tt.a,{variant:"middle"}),a.a.createElement($e.a,{onClick:this.handleClose,color:"primary"},"Close")))}}]),t}(a.a.Component),rt=Object(l.b)((function(e,t){return null!==e.currentDownloadStatus.lastError?{error:e.currentDownloadStatus.lastError}:{error:null}}))(Object(k.withStyles)((function(e){return{dialogContent:{padding:2*e.spacing.unit}}}))(nt));n(391);function at(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function ot(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?at(Object(n),!0).forEach((function(t){Object(i.a)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):at(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var ct=function(e){function t(){var e,n;Object(R.a)(this,t);for(var r=arguments.length,a=new Array(r),o=0;o<r;o++)a[o]=arguments[o];return(n=Object(_.a)(this,(e=Object(w.a)(t)).call.apply(e,[this].concat(a)))).state={query:"",queryFilter:"file_path",openModule:!1,moduleTarget:null},n.componentDidMount=function(){return n.props.onLoad()},n}return Object(P.a)(t,e),Object(v.a)(t,[{key:"render",value:function(){var e=this.props,t=e.classes,n=e.query;return a.a.createElement("div",{className:t.root},a.a.createElement(x.a,{container:!0,direction:"row",justify:"center",alignItems:"center",spacing:16,className:t.search_box},a.a.createElement(x.a,{item:!0,xs:8},a.a.createElement(He,null))),n?a.a.createElement(pe,null):a.a.createElement(Le,null),a.a.createElement(rt,null))}}]),t}(a.a.Component),lt=Object(k.withStyles)((function(e){return{root:{flexGrow:1,backgroundColor:e.palette.background.paper},search_box:{marginTop:4*e.spacing.unit,marginBottom:4*e.spacing.unit,width:"100%"},search_result:ot({},e.mixins.gutters(),{paddingTop:2*e.spacing.unit,paddingBottom:2*e.spacing.unit,marginLeft:8*e.spacing.unit,marginRight:8*e.spacing.unit}),module_box:{marginBottom:2*e.spacing.unit},noMaxWidth:{maxWidth:"none"}}}))(Object(l.b)((function(e,t){return{query:e.queryFilter}}),(function(e){return{onLoad:function(){e({type:f})}}}))(ct));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var st=n(13),ut=n.n(st),it=n(12),dt=n(47),pt=n.n(dt),Et=ut.a.mark(jt),ft=ut.a.mark(Rt),mt=ut.a.mark(_t),bt=ut.a.mark(wt),Ot=ut.a.mark(Pt),ht=ut.a.mark(kt),yt=ut.a.mark(Dt),gt=ut.a.mark(xt);function jt(e){return ut.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,Object(it.b)(it.c,500);case 2:return e.type=d,t.next=5,Object(it.d)(e);case 5:case"end":return t.stop()}}),Et)}function Rt(){return ut.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(it.f)(p,jt);case 2:case"end":return e.stop()}}),ft)}function vt(){return pt.a.get("/module").then((function(e){return e.body}))}function _t(e){var t;return ut.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=3,Object(it.e)(f);case 3:return e.prev=3,e.next=6,Object(it.b)(vt);case 6:if(t=e.sent){e.next=11;break}return e.next=10,Object(it.d)({type:b});case 10:return e.abrupt("continue",0);case 11:return t.map((function(e){return Array.isArray(e.folders)&&(e.folders_search=e.folders.join("/")),e})),e.next=14,Object(it.d)({type:m,modules:t});case 14:e.next=20;break;case 16:return e.prev=16,e.t0=e.catch(3),e.next=20,Object(it.d)({type:b});case 20:e.next=0;break;case 22:case"end":return e.stop()}}),mt,null,[[3,16]])}function wt(){var e;return ut.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:e=ut.a.mark((function e(){var t,n,r;return ut.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(it.e)("PREPARE_FOLDER_REQUEST");case 2:return t=e.sent,n=t.folders,e.prev=4,e.next=7,Object(it.b)((function(){return pt.a.get("/folder/".concat(n.join("-"),"/download")).then((function(e){return e.body}))}));case 7:if(!(r=e.sent).hasOwnProperty("error")){e.next=13;break}return e.next=11,Object(it.d)({type:"PREPARE_FOLDER_ERROR",error:r.error});case 11:e.next=16;break;case 13:return e.next=15,Object(it.d)({type:"PREPARE_FOLDER_RECEIVED",response:r});case 15:window.location.href="/download/".concat(r.uuid);case 16:e.next=22;break;case 18:return e.prev=18,e.t0=e.catch(4),e.next=22,Object(it.d)({type:"PREPARE_FOLDER_REQUEST_ERROR",error:e.t0});case 22:case"end":return e.stop()}}),e,null,[[4,18]])}));case 1:return t.delegateYield(e(),"t0",3);case 3:t.next=1;break;case 5:case"end":return t.stop()}}),bt)}function Pt(){var e;return ut.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:e=ut.a.mark((function e(){var t,n,r;return ut.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(it.e)("PREPARE_MODULE_REQUEST");case 2:return t=e.sent,n=t.module_key,e.prev=4,e.next=7,Object(it.b)((function(){return pt.a.get("/module/".concat(n,"/download")).then((function(e){return e.body}))}));case 7:if(!(r=e.sent).hasOwnProperty("error")){e.next=13;break}return e.next=11,Object(it.d)({type:"PREPARE_MODULE_ERROR",error:r.error});case 11:e.next=16;break;case 13:return e.next=15,Object(it.d)({type:"PREPARE_MODULE_RECEIVED",response:r});case 15:window.location.href="/download/".concat(r.uuid);case 16:e.next=22;break;case 18:return e.prev=18,e.t0=e.catch(4),e.next=22,Object(it.d)({type:"PREPARE_MODULE_REQUEST_ERROR",error:e.t0});case 22:case"end":return e.stop()}}),e,null,[[4,18]])}));case 1:return t.delegateYield(e(),"t0",3);case 3:t.next=1;break;case 5:case"end":return t.stop()}}),Ot)}function kt(){var e;return ut.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:e=ut.a.mark((function e(){var t,n,r;return ut.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(it.e)("PREPARE_PDF_REQUEST");case 2:return t=e.sent,n=t.module_key,e.prev=4,e.next=7,Object(it.b)((function(){return pt.a.get("/module/".concat(n,"/pdf")).then((function(e){return e.body}))}));case 7:if(!(r=e.sent).hasOwnProperty("error")){e.next=13;break}return e.next=11,Object(it.d)({type:"PREPARE_PDF_REQUEST_ERROR",error:r.error});case 11:e.next=16;break;case 13:return e.next=15,Object(it.d)({type:"PREPARE_PDF_RECEIVED",response:r});case 15:window.location.href="/download-pdf/".concat(r.uuid);case 16:e.next=22;break;case 18:return e.prev=18,e.t0=e.catch(4),e.next=22,Object(it.d)({type:"PREPARE_PDF_REQUEST_ERROR",error:e.t0});case 22:case"end":return e.stop()}}),e,null,[[4,18]])}));case 1:return t.delegateYield(e(),"t0",3);case 3:t.next=1;break;case 5:case"end":return t.stop()}}),ht)}function Dt(){var e;return ut.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:e=ut.a.mark((function e(){var t,n;return ut.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(it.e)("EDIT_MODULE_REQUEST");case 2:return t=e.sent,n=t.module_key,e.next=6,Object(it.b)((function(){return pt.a.get("/module/".concat(n,"/edit")).then((function(e){return e.body}))}));case 6:case"end":return e.stop()}}),e)}));case 1:return t.delegateYield(e(),"t0",3);case 3:t.next=1;break;case 5:case"end":return t.stop()}}),yt)}function xt(){return ut.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(it.a)([wt(),Pt(),kt(),Rt(),_t(),Dt()]);case 2:case"end":return e.stop()}}),gt)}var At=Object(u.a)(),St=window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__||s.d,Ct=Object(s.e)(j,St(Object(s.a)(At)));At.run(xt),c.a.render(a.a.createElement(l.a,{store:Ct},a.a.createElement(lt,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[165,1,2]]]);
//# sourceMappingURL=main.b155117b.chunk.js.map