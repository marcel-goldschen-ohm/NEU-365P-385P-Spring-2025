import {makeProject} from '@motion-canvas/core';

import pythonCrashCourse from './scenes/python-crash-course?scene';
// import programmingPartOfToolkit from './scenes/programming-part-of-toolkit?scene';
// import example from './scenes/example?scene';
// import example2 from './scenes/example2?scene';

import {Code, LezerHighlighter} from '@motion-canvas/2d';
import {parser} from '@lezer/python';
Code.defaultHighlighter = new LezerHighlighter(parser);

export default makeProject({
  scenes: [
    pythonCrashCourse,
    // programmingPartOfToolkit,
  ],
});
