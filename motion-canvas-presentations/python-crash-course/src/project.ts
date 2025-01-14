import {makeProject} from '@motion-canvas/core';

import pythonCrashCourse from './scenes/python-crash-course?scene';

// import {Code, LezerHighlighter} from '@motion-canvas/2d';
// import {parser} from '@lezer/python';
// import {HighlightStyle} from '@codemirror/language';
// import {tags} from '@lezer/highlight';
// import {vscodeLightStyle as codeStyle} from '@uiw/codemirror-theme-vscode';
// // for (const style of codeStyle) {
// //   console.log(style.tag.toString(), style.color);
// // }
// // codeStyle.push({tag: tags.special(tags.punctuation), color: '#393a42'});
// const codeTheme = HighlightStyle.define(codeStyle);
// Code.defaultHighlighter = new LezerHighlighter(parser, codeTheme);

export default makeProject({
  scenes: [
    pythonCrashCourse
  ],
});
