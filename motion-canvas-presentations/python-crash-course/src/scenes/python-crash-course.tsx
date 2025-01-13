import {is, makeScene2D, Circle, Code, Img, Layout, Line, Node, Ray, Rect, Txt} from '@motion-canvas/2d';
import {beginSlide, createRef, createSignal, DEFAULT, Reference, Vector2} from '@motion-canvas/core';
import {all, sequence, waitFor, waitUntil} from '@motion-canvas/core/lib/flow';
import {useLogger} from '@motion-canvas/core';
import {Colors, Terminal, Window} from '@hhenrichsen/canvas-commons';

export default makeScene2D(function* (view) {
  const logger = useLogger();

  const UT_BURNT_ORANGE = 'rgb(204, 102, 0)';
  const shellOutputStyle = {
    fontSize: 36,
    fontFamily: 'Monospace',
    fill: 'rgb(192, 192, 192)'
  };

  const learningGoals = [
      "\u2022 You will be able to manage Python environments.",
      "\u2022 You will understand basic Python syntax.",
      "\u2022 You will be able to translate your ideas into code.",
  ]

  const backgroundImg = createRef<Img>();
  view.add(<Img ref={backgroundImg} src={'../../images/backgrounds/UT-light-blue-2023-bg-only.png'} width={'100%'} height={'100%'} />);

  const containerLayout = createRef<Layout>();
  const headerLayout = createRef<Layout>();
  const mainLayout = createRef<Layout>();
  const footerLayout = createRef<Layout>();

  const headerLeftLayout = createRef<Layout>();
  const headerCenterLayout = createRef<Layout>();
  const headerRightLayout = createRef<Layout>();

  const footerLeftLayout = createRef<Layout>();
  const footerCenterLayout = createRef<Layout>();
  const footerRightLayout = createRef<Layout>();

  const titleTxt = createRef<Txt>();
  const footerTxt = createRef<Txt>();
  var titleStr = '?';
  var footerStr = '?';

  // Temporary Nodes added to the view
  var tmpNodes: Reference<Node>[] = [];

  view.add(
    <Layout ref={containerLayout} direction={'column'} width={'100%'} height={'100%'} padding={20} gap={20} layout>
      <Layout ref={headerLayout} direction={'row'} justifyContent={'center'} alignItems={'center'}>
        <Layout ref={headerLeftLayout} direction={'row'} justifyContent={'start'} alignItems={'start'}>
        </Layout>
        <Layout ref={headerCenterLayout} grow={1} direction={'row'} justifyContent={'center'} alignItems={'center'}>
          <Txt ref={titleTxt} text={titleStr} fontSize={72} textAlign={'center'} opacity={0} />
        </Layout>
        <Layout ref={headerRightLayout} direction={'row'} justifyContent={'end'} alignItems={'start'}>
        </Layout>
      </Layout>
      <Layout ref={mainLayout} grow={1} justifyContent={'center'} alignItems={'center'}>
      </Layout>
      <Layout ref={footerLayout} direction={'row'} justifyContent={'center'} alignItems={'center'}>
        <Layout ref={footerLeftLayout} direction={'row'} justifyContent={'start'} alignItems={'end'}>
        </Layout>
        <Layout ref={footerCenterLayout} grow={1} direction={'row'} justifyContent={'center'} alignItems={'center'}>
          <Txt ref={footerTxt} text={footerStr} fontSize={56} textAlign={'center'} opacity={0} />
        </Layout>
        <Layout ref={footerRightLayout} direction={'row'} justifyContent={'end'} alignItems={'end'}>
        </Layout>
      </Layout>
    </Layout>
  );

  // -------------------------------------------------------
  { titleStr = 'Python Crash Course';
    footerStr = 'Just about everything you will need to start using Python in 2025.';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').opacity(1).text(titleStr, 1);
    // content
    const pythonLogo = createRef<Img>();
    mainLayout().add(
      <Img ref={pythonLogo} src={'../../images/logos/python-logo.png'} height={500} opacity={0} />
    );
    yield* pythonLogo().opacity(1, 1);
    // write footer
    if (footerStr.length > 0) yield* footerTxt().text('').opacity(1).text(footerStr, 1);
  }

  // -------------------------------------------------------
  { titleStr = 'Programming: Part of a modern scientist\'s toolkit';
    footerStr = 'Datasets too large/complex to handle manually.';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const imagesNode = createRef<Node>();
    mainLayout().direction('row');
    mainLayout().add(
      <Node ref={imagesNode} opacity={0}>
        <Img src={'../../images/omics-cube.png'} width={'30%'} margin={20} />
        <Img src={'../../images/brain-connections.png'} width={'30%'} margin={20} />
        <Img src={'../../images/eeg-waveforms.png'} width={'30%'} margin={20} />
      </Node>
    );
    yield* imagesNode().opacity(1, 1);
    // write footer
    if (footerStr.length > 0) yield* footerTxt().text('').opacity(1).text(footerStr, 1);
  }

  // -------------------------------------------------------
  { titleStr = 'Interpreted vs Compiled';
    footerStr = '';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const sourceToMachineCodeLayout = createRef<Layout>();
    const sourceCodeImg = createRef<Img>();
    const machineCodeImg = createRef<Img>();
    const compileArrow = createRef<Ray>();
    const humanImg = createRef<Img>();
    const robotImg = createRef<Img>();
    mainLayout().direction('column');
    mainLayout().add(
      <Layout ref={sourceToMachineCodeLayout} direction={'row'} justifyContent={'center'} alignItems={'center'} opacity={0}>
        <Img ref={humanImg} src={'../../images/human.png'} width={400} margin={20} />
        <Img ref={sourceCodeImg} src={'../../images/source-code-file.png'} height={400} margin={20} />
        <Ray ref={compileArrow} endArrow lineWidth={12} arrowSize={30} stroke={'rgb(50, 50, 50)'} from={[0, 0]} to={[200, 0]} />
        <Img ref={machineCodeImg} src={'../../images/machine-code-file.png'} height={400} margin={20} />
        <Img ref={robotImg} src={'../../images/robot.png'} width={200} margin={20} marginRight={220} />
      </Layout>
    );
    const sourceCodeBullets = [createRef<Layout>(), createRef<Layout>(), createRef<Layout>()];
    const machineCodeBullets = [createRef<Layout>(), createRef<Layout>(), createRef<Layout>()];
    mainLayout().add(
      <Layout direction={'row'} gap={240}>
        <Layout direction={'column'} alignItems={'start'}>
          <Layout ref={sourceCodeBullets[0]} direction={'row'} alignItems={'center'} opacity={0}>
            <Img src={'../../images/icons/thumbs-up.png'} width={100} margin={20} />
            <Txt text={'Humans understand'} fontSize={42} fill={'rgb(0, 150, 255)'} />
          </Layout>
          <Layout ref={sourceCodeBullets[1]} direction={'row'} alignItems={'center'} opacity={0}>
            <Img src={'../../images/icons/thumbs-up.png'} width={100} margin={20} />
            <Txt text={'Runs everywhere'} fontSize={42} fill={'rgb(0, 150, 255)'} />
          </Layout>
          <Layout ref={sourceCodeBullets[2]} direction={'row'} alignItems={'center'} opacity={0}>
            <Img src={'../../images/icons/thumbs-down.png'} width={100} margin={20} />
            <Txt text={'Non-optimized execution'} fontSize={42} fill={'rgb(255, 0, 0)'} />
          </Layout>
        </Layout>
        <Layout direction={'column'} alignItems={'start'}>
          <Layout ref={machineCodeBullets[0]} direction={'row'} alignItems={'center'} opacity={0}>
            <Img src={'../../images/icons/thumbs-down.png'} width={100} margin={20} />
            <Txt text={'Humans don\'t understand'} fontSize={42} fill={'rgb(255, 0, 0)'} />
          </Layout>
          <Layout ref={machineCodeBullets[1]} direction={'row'} alignItems={'center'} opacity={0}>
            <Img src={'../../images/icons/thumbs-down.png'} width={100} margin={20} />
            <Txt text={'Runs only on specific hardware'} fontSize={42} fill={'rgb(255, 0, 0)'} />
          </Layout>
          <Layout ref={machineCodeBullets[2]} direction={'row'} alignItems={'center'} opacity={0}>
            <Img src={'../../images/icons/thumbs-up.png'} width={100} margin={20} />
            <Txt text={'Optimized execution'} fontSize={42} fill={'rgb(0, 150, 255)'} />
          </Layout>
        </Layout>
      </Layout>
    );
    yield* sourceToMachineCodeLayout().opacity(1, 1);
    for (let i = 0; i < 3; i++) {
      yield* beginSlide('');
      yield* all(
        sourceCodeBullets[i]().opacity(1, 1),
        machineCodeBullets[i]().opacity(1, 1),
      );
    }
    // write title
    yield* beginSlide('');
    yield* titleTxt().text('').text("Python = Syntax + Interpreter", 1);
    // highlight syntax and interpreter steps
    const dt = 0.5;
    for (let i = 0; i < 3; i++) {
      yield* all(
        sourceCodeImg().shadowOffset(20, dt).to(0, dt),
        sourceCodeImg().shadowBlur(20, dt).to(0, dt),
        sourceCodeImg().shadowColor('rgb(255, 255, 0)', dt).to(DEFAULT, dt),
        compileArrow().stroke('rgb(255, 255, 0)', dt).to('rgb(50, 50, 50)', dt),
        compileArrow().lineWidth(18, dt).to(12, dt),
        compileArrow().arrowSize(45, dt).to(30, dt),
      );
    }
  }

  // -------------------------------------------------------
  { titleStr = 'Python Interpreters (Flavors)';
    footerStr = 'We will use the standard CPython interpreter.';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const flavorsImg = createRef<Img>();
    mainLayout().add(
      <Img ref={flavorsImg} src={'../../images/python-flavors.png'} height={'82%'} margin={20} opacity={0} />
    );
    yield* flavorsImg().opacity(1, 1);
    yield* waitFor(1);
    // circle CPython
    const circleNode = createRef<Node>();
    const circle = createRef<Circle>();
    view.add(
      <Node ref={circleNode}>
        <Circle ref={circle} x={-220} y={-282} width={450} height={120} lineWidth={10} stroke={UT_BURNT_ORANGE} startAngle={-180} endAngle={180} opacity={0} />
      </Node>
    );
    tmpNodes.push(circleNode);
    // write footer and draw circle
    yield* all(
      circle().endAngle(-180).opacity(1).endAngle(180, 0.5),
      footerTxt().text('').opacity(1).fill(UT_BURNT_ORANGE).text(footerStr, 1),
    );
  }

  // -------------------------------------------------------
  { titleStr = 'Some Alternatives to Python';
    footerStr = '[]';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const logosNode = createRef<Node>();
    mainLayout().direction('row');
    mainLayout().add(
      <Node ref={logosNode} opacity={0}>
        <Img src={'../../images/logos/matlab-logo.png'} width={'20%'} margin={50} />
        <Img src={'../../images/logos/R-logo.png'} width={'20%'} margin={50} />
        <Img src={'../../images/logos/julia-logo.png'} width={'20%'} margin={50} />
      </Node>
    );
    yield* logosNode().opacity(1, 1);
  }

  // -------------------------------------------------------
  { titleStr = 'Learning Goals';
    footerStr = '[]';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    mainLayout().direction('column');
    const bmiImg = createRef<Img>();
    mainLayout().add(
      <Img ref={bmiImg} src={'../../images/logos/brain-machine-interface-logo.png'} height={150} margin={20} opacity={0} />
    );
    const goalsLayout = createRef<Layout>();
    mainLayout().add(
      <Layout ref={goalsLayout} grow={1}  direction={'column'} justifyContent={'start'} alignItems={'start'} padding={40} gap={40}></Layout>
    );
    const goals: Reference<Txt>[] = [];
    for (let i = 0; i < learningGoals.length; i++) {
      goals.push(createRef<Txt>());
      goalsLayout().add(
        <Txt ref={goals[i]} text={learningGoals[i]} fontSize={60} textWrap={true} opacity={0} />
      );
    }
    yield* all(
      bmiImg().opacity(1, 1),
      ...goals.map((goal) => goal().opacity(0.1, 1)),
    );
    yield* goals[0]().opacity(1, 1);
  }

  // -------------------------------------------------------
  { titleStr = 'Python Package Ecosystem';
    footerStr = 'One of the primary reasons for choosing Python.';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const packagesImg = createRef<Img>();
    mainLayout().add(
      <Img ref={packagesImg} src={'../../images/python-package-ecosystem.png'} height={'82%'} margin={20} opacity={0} />
    );
    yield* packagesImg().opacity(1, 1);
    // circle and many many more
    const circleNode = createRef<Node>();
    const circle = createRef<Circle>();
    view.add(
      <Node ref={circleNode}>
        <Circle ref={circle} x={585} y={120} width={240} height={150} lineWidth={10} stroke={UT_BURNT_ORANGE} startAngle={-180} endAngle={180} opacity={0} />
      </Node>
    );
    tmpNodes.push(circleNode);
    yield* circle().endAngle(-180).opacity(1).endAngle(180, 0.5);
    // write footer
    if (footerStr.length > 0) yield* footerTxt().text('').fill(DEFAULT).opacity(1).text(footerStr, 1);
    // blink circle
    const dt = 0.5;
    for (let i = 0; i < 3; i++) {
      yield* circle().lineWidth(0, dt).to(10, dt);
    }
  }

  // -------------------------------------------------------
  { titleStr = 'Package Dependency Graph';
    footerStr = 'Dependencies can be version specific.';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    mainLayout().direction('row');
    const graphImg = createRef<Img>();
    mainLayout().add(
      <Img ref={graphImg} src={'../../images/package-dependency-graph.png'} height={'75%'} margin={20} opacity={0} />
    );
    yield* graphImg().opacity(1, 1);
    // write footer: version specific
    yield* beginSlide('');
    yield* footerTxt().text('').opacity(1).text(footerStr, 1);
    // write footer: conflict
    yield* beginSlide('');
    footerStr = 'What if zlib needs sqlite 2.1 and ncurses needs sqlite 3.0?';
    const v2 = createRef<Node>();
    const v3 = createRef<Node>();
    view.add(
      <Node ref={v2} position={[280, 20]} opacity={0}>
        <Txt text={'2.1'} fontSize={76} fill={'rgb(255, 0, 0)'} />
      </Node>
    );
    view.add(
      <Node ref={v3} position={[330, 120]} opacity={0}>
        <Txt text={'3.0'} fontSize={76} fill={'rgb(255, 0, 0)'} />
      </Node>
    );
    tmpNodes.push(v2, v3);
    yield* all(
      footerTxt().text('').opacity(1).text(footerStr, 1),
      v2().opacity(1, 1),
      v3().opacity(1, 1),
    );
    // write footer: conflict!
    yield* beginSlide('');
    const xmark = createRef<Node>();
    view.add(
      <Node ref={xmark} position={[430, -78]} opacity={0}>
        <Line lineWidth={10} points={[[-65, -65], [65, 65]]} stroke={'rgb(255, 0, 0)'} />
        <Line lineWidth={10} points={[[-65, 65], [65, -65]]} stroke={'rgb(255, 0, 0)'} />
      </Node>
    );
    tmpNodes.push(xmark);
    yield* all(
      footerTxt().text('').opacity(1).fill('rgb(255, 0, 0)').text('Conflict!', 1),
      xmark().opacity(1, 1),
    );
    // write footer: when not it
    yield* beginSlide('');
    footerStr = 'It\'s not IF you will get a dependency conflict, but WHEN.';
    yield* footerTxt().text('').opacity(1).fill(DEFAULT).text(footerStr, 1);
  }

  // -------------------------------------------------------
  { titleStr = 'Package Managers';
    footerStr = 'Managing dependencies is NOT for humans!';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    mainLayout().direction('row');
    const graphLayout = createRef<Layout>();
    mainLayout().add(
      <Layout ref={graphLayout} direction={'column'} justifyContent={'center'} alignItems={'center'} padding={50} width={'50%'} height={'100%'} opacity={1}>
        <Txt text={'Python package dependency graph'} fontSize={36} fill={'rgb(100, 100, 100)'} />
        <Img src={'../../images/python-dependency-graph.png'} height={'75%'} margin={20} />
      </Layout>
    );
    mainLayout().add(
      <Layout ref={graphLayout} direction={'column'} justifyContent={'center'} alignItems={'center'} padding={50} width={'50%'} height={'100%'}>
      </Layout>
    );
    const tmpNode = createRef<Node>();
    const managersTxt = createRef<Txt>();
    const logosNode = createRef<Node>();
    const pipLogo = createRef<Img>();
    const condaLogo = createRef<Img>();
    const pdmLogo = createRef<Img>();
    const poetryLogo = createRef<Img>();
    const mamabaLogo = createRef<Img>();
    const hatchLogo = createRef<Img>();
    const andMoreTxt = createRef<Txt>();
    view.add(
      <Node ref={tmpNode}>
        <Txt ref={managersTxt} fontSize={48} textWrap={true} width={900} offset={[-1, -1]} position={[0, -300]} />
        <Node ref={logosNode} opacity={0} >
          <Img ref={pipLogo} src={'../../images/logos/pip-logo.png'} height={100} margin={20} offset={[-1, -1]} position={[0, -130]} />
          <Img ref={condaLogo} src={'../../images/logos/conda-logo.png'} height={100} margin={20} offset={[-1, -1]} position={[pipLogo().right().x + 50, pipLogo().top().y]} />
          <Img ref={pdmLogo} src={'../../images/logos/pdm-logo.png'} height={100} margin={20} offset={[-1, -1]} position={[0, 20]} />
          <Img ref={poetryLogo} src={'../../images/logos/poetry-logo.png'} height={100} margin={20} offset={[-1, -1]} position={[pdmLogo().right().x + 50, pdmLogo().top().y]} />
          <Img ref={mamabaLogo} src={'../../images/logos/mamba-logo.png'} height={100} margin={20} offset={[-1, -1]} position={[0, 150]} />
          <Img ref={hatchLogo} src={'../../images/logos/hatch-logo.png'} height={100} margin={20} offset={[-1, -1]} position={[mamabaLogo().right().x + 50, mamabaLogo().top().y]} />
        </Node>
        <Txt ref={andMoreTxt} fontSize={48} fill={UT_BURNT_ORANGE} offset={[-1, -1]} position={[hatchLogo().right().x + 50, hatchLogo().top().y + 40]} />
      </Node>
    );
    tmpNodes.push(tmpNode);
    // show graph
    yield* graphLayout().opacity(1, 1);
    // write footer
    yield* footerTxt().text('').opacity(1).fill(DEFAULT).text(footerStr, 1);
    // show package managers
    yield* beginSlide('');
    yield* managersTxt().text('Fortunately, we have package managers for this...', 1);
    yield* logosNode().opacity(1, 1);
    yield* andMoreTxt().text('... and more...', 1);
    // conda and pip
    yield* beginSlide('');
    pdmLogo().remove();
    poetryLogo().remove();
    mamabaLogo().remove();
    hatchLogo().remove();
    andMoreTxt().remove();
    yield* all(
      managersTxt().text('').text('We\'ll use conda and pip, but you are free to use any package manager you like.', 1),
      condaLogo().x(pipLogo().x(), 1),
      pipLogo().y(pipLogo().y() + 200, 1),
      pipLogo().height(150, 1),
      condaLogo().height(150, 1),
    );
  }

  // -------------------------------------------------------
  { titleStr = 'Install Conda';
    footerStr = 'https://github.com/conda-forge/miniforge';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    mainLayout().direction('row');
    const installLayout = createRef<Layout>();
    mainLayout().add(
      <Layout ref={installLayout} direction={'column'} justifyContent={'center'} alignItems={'center'} width={'45%'} padding={25} opacity={0}>
        <Txt text={'In 2025, I recommend installing'} fontSize={56} />
        <Txt.b text={'miniforge'} fontSize={56} fill={UT_BURNT_ORANGE} margin={10} />
        <Txt text={'which includes conda.'} fontSize={56} />
      </Layout>
    );
    yield* installLayout().opacity(1, 1);
    // write footer
    if (footerStr.length > 0) yield* footerTxt().text('').opacity(1).fill(DEFAULT).text(footerStr, 1);
  }

  // -------------------------------------------------------
  { titleStr = 'Using Conda';
    footerStr = 'https://github.com/conda-forge/miniforge';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer visible
    footerTxt().opacity(1).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const terminal = createRef<Terminal>();
    const terminalWindow = createRef<Window>();
    const terminalNode = createRef<Node>();
    yield view.add(
      <Node ref={terminalNode}>
        <Window
          ref={terminalWindow}
          title={'Terminal'}
          size={[1400, 800]}
          headerColor={Colors.Catppuccin.Mocha.Base}
          bodyColor={Colors.Catppuccin.Mocha.Mantle}
          buttonColors={[
            Colors.Catppuccin.Mocha.Red,
            Colors.Catppuccin.Mocha.Yellow,
            Colors.Catppuccin.Mocha.Green,
          ]}
          icon={'ph:terminal'}
        >
          <Terminal
            ref={terminal}
            defaultTxtProps={{fontFamily: 'Ellograph CF', fontSize: 50}}
            padding={20}
          />
        </Window>
      </Node>
    );
    const terminalPrefixSymbol = terminal().prefix();
    terminal().prefix({text: '' + terminalPrefixSymbol, fill: UT_BURNT_ORANGE});
    tmpNodes.push(terminalNode);
    yield* terminalWindow().open(view, 1);
    yield* terminal().typeLine('', 1); // show prompt

    yield* terminal().typeAfterLine('conda --version', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: 'conda 24.7.1', ...shellOutputStyle});
    terminal().lineAppear({text: ' ', ...shellOutputStyle});
    yield* waitFor(1);
    yield* terminal().typeLine('', 1);

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda --help', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: 'usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...', ...shellOutputStyle});
    terminal().lineAppear({text: ' ', ...shellOutputStyle});
    terminal().lineAppear({text: 'conda is a tool for managing and deploying applications,', ...shellOutputStyle});
    terminal().lineAppear({text: '    environments and packages.', ...shellOutputStyle});
    terminal().lineAppear({text: ' ', ...shellOutputStyle});
    terminal().lineAppear({text: '...', ...shellOutputStyle});
    terminal().lineAppear({text: ' ', ...shellOutputStyle});
    yield* waitFor(1);
    yield* terminal().typeLine('', 1); // show prompt

    // // close terminal
    // yield* beginSlide('');
    // yield* terminalWindow().close(view, 1);
  }

  // -------------------------------------------------------
  { titleStr = 'Virtual Environments';
    footerStr = '[]';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    mainLayout().direction('row');

    var venvFolders: Reference<Img>[] = [];
    for (let i = 0; i < 3; i++) {
      venvFolders.push(createRef<Img>());
      mainLayout().add(
        <Img ref={venvFolders[i]} src={'../../images/folder.png'} width={'30%'} margin={20} opacity={0} />
      );
    }

    var venvPackageLayouts: Reference<Layout>[] = [];
    for (let i = 0; i < 3; i++) {
      venvPackageLayouts.push(createRef<Layout>());
      view.add(
        <Layout ref={venvPackageLayouts[i]} direction={'row'} justifyContent={'center'} alignItems={'end'} layout>
          <Img src={'../../images/logos/python-logo.png'} width={125} margin={20} />
          {i == 2 ? <Img src={'../../images/logos/jupyter-logo.png'} width={125} margin={20} /> : <Img src={'../../images/logos/numpy-logo.png'} width={125} margin={20} />}
          {i == 1 ? <Img src={'../../images/logos/jupyter-logo.png'} width={125} margin={20} /> : <Img src={'../../images/logos/scipy-logo.png'} width={125} margin={20} />}
        </Layout>
      );
      tmpNodes.push(venvPackageLayouts[i]);
      // position just off screen above folders
      venvPackageLayouts[i]().absolutePosition([venvFolders[i]().absolutePosition().x, -200]);
    }

    const venvTxt = createRef<Txt>();
    view.add(
      <Txt ref={venvTxt} fontSize={56} textWrap={true} width={900} offset={[-1, -1]} position={[-200, -100]} />
    );
    tmpNodes.push(venvTxt);

    yield* all(
      venvFolders[0]().opacity(1, 1),
      venvTxt().text('A virtual environment is essentially just a folder on your computer where you will store a particular collection of python packages.', 1),
    );

    yield* beginSlide('');
    yield* all(
      footerTxt().text('').opacity(1).fill(DEFAULT).text('You can have as many virtual environments as you want.', 1),
      venvTxt().opacity(0, 1),
      venvFolders[1]().opacity(1, 1),
      venvFolders[2]().opacity(1, 1),
    );

    yield* beginSlide('');
    yield* all(
      footerTxt().text('').opacity(1).fill(DEFAULT).text('Each one can have a different collection of packages.', 1),
      ...venvPackageLayouts.map((layout, i) => layout().y(venvFolders[i]().position().y, 1)),
    );

    yield* beginSlide('');
    const numpyVersionsTxt: Reference<Txt>[] = [];
    ['2.0', '1.2'].map((version, i) => {
      numpyVersionsTxt.push(createRef<Txt>());
      view.add(
        <Txt ref={numpyVersionsTxt[i]} text={version} fontSize={56} offset={[0, -1]} paddingTop={20} opacity={0} />
      );
      tmpNodes.push(numpyVersionsTxt[i]);
      const logo = venvPackageLayouts[i]().findAll(is(Img))[1];
      numpyVersionsTxt[i]().absolutePosition([logo.absolutePosition().x, logo.absolutePosition().y + 75]);
    });
    yield* all(
      footerTxt().text('').opacity(1).fill(DEFAULT).text('Or different versions of the same package.', 1),
      ...numpyVersionsTxt.map((txt) => txt().opacity(1, 1)),
    );

    yield* beginSlide('');
    const pythonVersionsTxt: Reference<Txt>[] = [];
    ['3.12', '2.10', '3.11'].map((version, i) => {
      pythonVersionsTxt.push(createRef<Txt>());
      view.add(
        <Txt ref={pythonVersionsTxt[i]} text={version} fontSize={56} offset={[0, -1]} paddingTop={20} opacity={0} />
      );
      tmpNodes.push(pythonVersionsTxt[i]);
      const logo = venvPackageLayouts[i]().findAll(is(Img))[0];
      pythonVersionsTxt[i]().absolutePosition([logo.absolutePosition().x, logo.absolutePosition().y + 75]);
    });
    yield* all(
      footerTxt().text('').opacity(1).fill(DEFAULT).text('Conda can even manage different versions of Python.', 1),
      ...pythonVersionsTxt.map((txt) => txt().opacity(1, 1)),
      ...numpyVersionsTxt.map((txt) => txt().opacity(0.1, 1)),
    );

    yield* beginSlide('');
    yield* all(
      footerTxt().text('').opacity(1).fill(DEFAULT).text('I strongly suggest each of your projects have its own environment.', 1),
      ...pythonVersionsTxt.map((txt) => txt().opacity(0.1, 1)),
    );

    yield* beginSlide('');
    yield* all(
      venvFolders[1]().opacity(0, 1),
      venvFolders[2]().opacity(0, 1),
      venvPackageLayouts[1]().opacity(0, 1),
      venvPackageLayouts[2]().opacity(0, 1),
      pythonVersionsTxt[1]().opacity(0, 1),
      pythonVersionsTxt[2]().opacity(0, 1),
      numpyVersionsTxt[1]().opacity(0, 1),
      venvTxt().text('').opacity(1).text('This way when you have a problem you can wipe and restore the environment without affecting your other projects.', 1),
    );

    yield* beginSlide('');
    const fileNode = createRef<Node>();
    view.add(
      <Node ref={fileNode} position={[-150, 0]} opacity={0}>
        <Img src={'../../images/file.png'} width={'10%'} margin={20} />
        <Txt fontSize={56} text={'.py\nscript'} textAlign={'center'} fill={'rgb(255, 255, 255)'} />
      </Node>
    );
    tmpNodes.push(fileNode);
    const scriptTxts: Reference<Txt>[] = [];
    scriptTxts.push(createRef<Txt>());
    view.add(
      <Txt ref={scriptTxts[0]} fontSize={56} offset={[-1, -1]} textWrap={true} position={[50, -250]} width={800} opacity={0}>
        Python scripts you write are <Txt.b>NOT</Txt.b> part of any environment.
      </Txt>
    );
    scriptTxts.push(createRef<Txt>());
    view.add(
      <Txt ref={scriptTxts[1]} fontSize={56} offset={[-1, -1]} textWrap={true} position={[50, -50]} width={800} />
    );
    scriptTxts.push(createRef<Txt>());
    view.add(
      <Txt ref={scriptTxts[2]} fontSize={56} fontStyle={'italic'} offset={[-1, -1]} textWrap={true} position={[50, 150]} width={800} fill={UT_BURNT_ORANGE} />
    );
    tmpNodes.push(...scriptTxts);
    yield* all(
      venvTxt().opacity(0, 1),
      footerTxt().opacity(0, 1),
      fileNode().opacity(1, 1),
      scriptTxts[0]().opacity(1, 1),
    );
    yield* scriptTxts[1]().text('Environments only contain the packages scripts depend on.', 1);
    yield* scriptTxts[2]().text('You select an environment to use when you run your scripts.', 1);
  }

  // -------------------------------------------------------
  { titleStr = 'Conda Virtual Environments';
    footerStr = '';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const terminalWindow = createRef<Window>();
    const terminal = createRef<Terminal>();
    yield view.add(
      <Window
        ref={terminalWindow}
        title={'Terminal'}
        size={[960, 900]}
        position={[-420, 40]}
        headerColor={Colors.Catppuccin.Mocha.Base}
        bodyColor={Colors.Catppuccin.Mocha.Mantle}
        buttonColors={[
          Colors.Catppuccin.Mocha.Red,
          Colors.Catppuccin.Mocha.Yellow,
          Colors.Catppuccin.Mocha.Green,
        ]}
        icon={'ph:terminal'}
      >
        <Terminal
          ref={terminal}
          defaultTxtProps={{fontFamily: 'Ellograph CF', fontSize: 50}}
          padding={20}
        />
      </Window>
    );
    tmpNodes.push(terminalWindow);
    const terminalPrefixSymbol = terminal().prefix();
    yield* terminalWindow().open(view, 1);

    const baseVenv = createRef<Node>();
    view.add(
      <Node ref={baseVenv} x={75} y={600}>
        <Img src={'../../images/folder.png'} width={'45%'} offset={[-1, -1]} margin={20} />
        <Txt text={'base'} fontSize={56} offset={[-1, -1]} x={60} y={10} />
      </Node>
    );
    tmpNodes.push(baseVenv);

    const myVenv = createRef<Node>();
    const myPackages = createRef<Txt>();
    const myPackageVersions = createRef<Txt>();
    view.add(
      <Node ref={myVenv} x={75} y={600}>
        <Img src={'../../images/folder.png'} width={'45%'} offset={[-1, -1]} margin={20} />
        <Txt text={'neu365p'} fontSize={56} offset={[-1, -1]} x={60} y={10} />
        <Txt ref={myPackages} fontSize={50} fontFamily={'Monospace'} offset={[-1, -1]} x={60} y={120} />
        <Txt ref={myPackageVersions} fontSize={50} fontFamily={'Monospace'} offset={[-1, -1]} x={400} y={120} />
      </Node>
    );
    tmpNodes.push(myVenv);

    terminal().prefix({text: '(base) ' + terminalPrefixSymbol, fill: UT_BURNT_ORANGE});
    yield* all(
      terminal().typeLine(' ', 1),
      baseVenv().y(-350, 1),
    );

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda env list', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: '# conda environments', ...shellOutputStyle});
    terminal().lineAppear({text: '#', ...shellOutputStyle});
    terminal().lineAppear({text: 'base     *  .../base', ...shellOutputStyle});
    yield* waitFor(1);
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('create --name neu365p', 2);
    yield* terminal().typeLine('', 1); // show prompt
    yield* myVenv().y(350, 1);

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda env list', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: '# conda environments', ...shellOutputStyle});
    terminal().lineAppear({text: '#', ...shellOutputStyle});
    terminal().lineAppear({text: 'base     *  .../base', ...shellOutputStyle});
    terminal().lineAppear({text: 'neu365      .../neu365', ...shellOutputStyle});
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda activate neu365p', 2);
    yield* all(
      baseVenv().y(350, 1),
      myVenv().y(-350, 1),
    );
    terminal().prefix({text: '(neu365p) ' + terminalPrefixSymbol, fill: UT_BURNT_ORANGE});
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda env list', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: '# conda environments', ...shellOutputStyle});
    terminal().lineAppear({text: '#', ...shellOutputStyle});
    terminal().lineAppear({text: 'base        .../base', ...shellOutputStyle});
    terminal().lineAppear({text: 'neu365   *  .../neu365', ...shellOutputStyle});

    yield* beginSlide('');
    for (let i = 0; i < 16; i++) {
      terminal().deleteLine();
    }
    yield* terminal().typeLine('', 1); // show prompt
    yield* terminal().typeAfterLine('conda install python', 2);
    yield* all(
      myPackages().text('pip\npython\n...', 1),
      myPackageVersions().text('24.3.1\n3.12.7', 1),
    );
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda install python=3.10', 2);
    yield* all(
      myPackages().text('pip\npython\n...', 1),
      myPackageVersions().text('24.3.1\n3.10.16', 1),
    );
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda install "python<3.12"', 2);
    yield* all(
      myPackages().text('pip\npython\n...', 1),
      myPackageVersions().text('24.3.1\n3.11.9', 1),
    );
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda list', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: '# packages in environment at neu365p', ...shellOutputStyle});
    terminal().lineAppear({text: '#', ...shellOutputStyle});
    terminal().lineAppear({text: '# Name     Version', ...shellOutputStyle});
    terminal().lineAppear({text: 'pip        24.3.1', ...shellOutputStyle});
    terminal().lineAppear({text: 'python     3.11.9', ...shellOutputStyle});
    terminal().lineAppear({text: '...', ...shellOutputStyle});
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    for (let i = 0; i < 11; i++) {
      terminal().deleteLine();
    }
    yield* all(
      titleTxt().text('').text('Pip Package Manager', 1),
      terminal().typeLine('', 1),
    );
    yield* terminal().typeAfterLine('pip --help', 2);
    terminal().lineAppear({text: ' ', ...shellOutputStyle});
    terminal().lineAppear({text: 'Usage:', ...shellOutputStyle});
    terminal().lineAppear({text: '  pip <commands> [options]', ...shellOutputStyle});
    terminal().lineAppear({text: ' ', ...shellOutputStyle});
    terminal().lineAppear({text: 'Commands:', ...shellOutputStyle});
    terminal().lineAppear({text: '...', ...shellOutputStyle});
    terminal().lineAppear({text: ' ', ...shellOutputStyle});
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    for (let i = 0; i < 9; i++) {
      terminal().deleteLine();
    }
    yield* terminal().typeLine('', 1),
    yield* terminal().typeAfterLine('pip install ipykernel', 2);
    yield* all(
      myPackages().text('ipykernel\npip\npython\n...', 1),
      myPackageVersions().text('6.29.5\n24.3.1\n3.12.7', 1),
    );
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('pip install ipykernel==6.10.0', 2);
    yield* all(
      myPackages().text('ipykernel\npip\npython\n...', 1),
      myPackageVersions().text('6.10.0\n24.3.1\n3.12.7', 1),
    );
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('pip install "ipykernel<=6.3"', 2);
    yield* all(
      myPackages().text('ipykernel\npip\npython\n...', 1),
      myPackageVersions().text('6.3.0\n24.3.1\n3.12.7', 1),
    );
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('pip list', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: 'Package     Version', ...shellOutputStyle});
    terminal().lineAppear({text: '----------- -----------', ...shellOutputStyle});
    terminal().lineAppear({text: 'ipykernel   6.3.0', ...shellOutputStyle});
    terminal().lineAppear({text: '...', ...shellOutputStyle});
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda list', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: '# packages in environment at neu365p', ...shellOutputStyle});
    terminal().lineAppear({text: '#', ...shellOutputStyle});
    terminal().lineAppear({text: '# Name     Version', ...shellOutputStyle});
    terminal().lineAppear({text: 'ipykernel  6.3.0', ...shellOutputStyle});
    terminal().lineAppear({text: 'pip        24.3.1', ...shellOutputStyle});
    terminal().lineAppear({text: 'python     3.11.9', ...shellOutputStyle});
    terminal().lineAppear({text: '...', ...shellOutputStyle});

    yield* beginSlide('');
    for (let i = 0; i < 16; i++) {
      terminal().deleteLine();
    }
    yield* terminal().typeLine('', 1); // show prompt
    yield* terminal().typeAfterLine('conda activate base', 2);
    yield* all(
      baseVenv().y(-350, 1),
      myVenv().y(350, 1),
    );
    terminal().prefix({text: '(base) ' + terminalPrefixSymbol, fill: UT_BURNT_ORANGE});
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda env remove --name neu365p', 2);
    yield* myVenv().y(600, 1);
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* terminal().typeAfterLine('conda env list', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: '# conda environments', ...shellOutputStyle});
    terminal().lineAppear({text: '#', ...shellOutputStyle});
    terminal().lineAppear({text: 'base     *  .../base', ...shellOutputStyle});
    yield* waitFor(1);
    yield* terminal().typeLine('', 1); // show prompt
  }

  // -------------------------------------------------------
  { titleStr = 'Python Files';
    footerStr = '[]';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const pythonFileNode = createRef<Node>();
    const jupyerNotebookFileNode = createRef<Node>();
    view.add(
      <Node ref={pythonFileNode} x={-300} y={-100} opacity={0}>
        <Img src={'../../images/file.png'} width={'15%'} margin={20} />
        <Txt fontSize={82} text={'.py'} textAlign={'center'} fill={'rgb(255, 255, 255)'} />
        <Txt fontSize={64} text={'Python\ntext file'} textAlign={'center'} offset={[0, -1]} y={300} fill={(UT_BURNT_ORANGE)} />
      </Node>
    );
    tmpNodes.push(pythonFileNode);
    view.add(
      <Node ref={jupyerNotebookFileNode} x={300} y={-100} opacity={0}>
        <Img src={'../../images/file.png'} width={'15%'} margin={20} />
        <Txt fontSize={82} text={'.ipynb'} textAlign={'center'} fill={'rgb(255, 255, 255)'} />
        <Txt fontSize={64} text={'IPython\nJupyter notebook'} textAlign={'center'} offset={[0, -1]} y={300} fill={(UT_BURNT_ORANGE)} />
      </Node>
    );
    tmpNodes.push(jupyerNotebookFileNode);

    yield* all(
      pythonFileNode().opacity(1, 1),
      jupyerNotebookFileNode().opacity(1, 1),
    );
  }

  // -------------------------------------------------------
  { titleStr = 'Run Python Scripts';
    footerStr = '[]';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const terminal = createRef<Terminal>();
    const terminalWindow = createRef<Window>();
    const terminalNode = createRef<Node>();
    yield view.add(
      <Node ref={terminalNode}>
        <Window
          ref={terminalWindow}
          title={'Terminal'}
          size={[1080, 900]}
          position={[-350, 40]}
          headerColor={Colors.Catppuccin.Mocha.Base}
          bodyColor={Colors.Catppuccin.Mocha.Mantle}
          buttonColors={[
            Colors.Catppuccin.Mocha.Red,
            Colors.Catppuccin.Mocha.Yellow,
            Colors.Catppuccin.Mocha.Green,
          ]}
          icon={'ph:terminal'}
        >
          <Terminal
            ref={terminal}
            defaultTxtProps={{fontFamily: 'Ellograph CF', fontSize: 50}}
            padding={20}
          />
        </Window>
      </Node>
    );
    const terminalPrefixSymbol = terminal().prefix();
    terminal().prefix({text: '(base) ' + terminalPrefixSymbol, fill: UT_BURNT_ORANGE});
    tmpNodes.push(terminalNode);
    yield* terminalWindow().open(view, 1);
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    const instructionsTxt = createRef<Txt>();
    view.add(
      <Txt ref={instructionsTxt} fontSize={56} textWrap={true} width={650} offset={[-1, -1]} position={[250, -300]} />
    );
    tmpNodes.push(instructionsTxt);
    yield* instructionsTxt().text('Remember to activate your desired environment before running your script.', 1);
    yield* terminal().typeAfterLine('conda activate neu365p', 2);
    terminal().prefix({text: '(neu365p) ' + terminalPrefixSymbol, fill: UT_BURNT_ORANGE});
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    const pythonScriptNode = createRef<Node>();
    view.add(
      <Node ref={pythonScriptNode} x={500} y={150} opacity={0}>
        <Img src={'../../images/file.png'} width={'15%'} margin={20} />
        <Txt fontSize={82} text={'.py'} textAlign={'center'} fill={'rgb(255, 255, 255)'} />
      </Node>
    );
    tmpNodes.push(pythonScriptNode);
    yield* all(
      instructionsTxt().text('').text('Navigate to the folder containing your *.py script.', 1),
      pythonScriptNode().opacity(1, 1),
    );
    yield* terminal().typeAfterLine('cd path/to/script.py', 2);
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* instructionsTxt().text('').text('Run the code in script.py using the active environment.', 1);
    yield* terminal().typeAfterLine('python script.py', 2);
    yield* terminal().typeLine('', 1); // show prompt

    yield* beginSlide('');
    yield* all(
      instructionsTxt().text('').text('Just like for conda and pip, you can query the python version and get usage instructions.', 1),
      pythonScriptNode().opacity(0, 1),
    );
    yield* terminal().typeAfterLine('python --version', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: 'Python 3.12.7', ...shellOutputStyle});
    yield* terminal().typeLine('', 1); // show prompt
    yield* terminal().typeAfterLine('python --help', 2);
    yield* waitFor(1);
    terminal().lineAppear({text: 'usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...', ...shellOutputStyle});
    terminal().lineAppear({text: '...', ...shellOutputStyle});
    terminal().lineAppear({text: ' ', ...shellOutputStyle});
    yield* terminal().typeLine('', 1); // show prompt
  }

  // -------------------------------------------------------
  // TODO: videos of VSCode actions
  { titleStr = 'Integrated Development Environments (IDEs)';
    footerStr = '[]';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    const msg = createRef<Txt>();
    view.add(
      <Txt ref={msg} fontSize={56} textWrap={true} width={1400} offset={[-1, -1]} position={[-700, 250]} />
    );
    tmpNodes.push(msg);
    yield* msg().text('Although you can do all your python code development with a simple text editor and a terminal, you may find it more convenient to use an IDE.', 1);
    const logos = [
      createRef<Img>(),
      createRef<Img>(),
      createRef<Img>(),
      createRef<Img>(),
    ];
    [
      '../../images/logos/vscode-logo.png',
      '../../images/logos/pycharm-logo.png',
      '../../images/logos/spyder-logo.png',
      '../../images/logos/jupyter-logo.png',
    ].map((src, i) => {
      view.add(
        <Img ref={logos[i]} src={src} height={200} margin={20} x={-500 + 300 * i} y={-700} />
      );
    });
    tmpNodes.push(...logos);
    yield* sequence(
      0.1,
      ...logos.map((logo) => logo().y(0, 1)),
    );
    const labels = [
      createRef<Txt>(),
      createRef<Txt>(),
      createRef<Txt>(),
      createRef<Txt>(),
    ];
    [
      'Visual\nStudio\nCode',
      'PyCharm',
      'Spyder',
      'JupyterLab'
    ].map((label, i) => {
      const txt = createRef<Txt>();
      view.add(
        <Txt ref={labels[i]} fontSize={48} text={label} textAlign={'center'} offset={[0, 1]} position={[-500 + 300 * i, -150]} opacity={0} />
      );
    });
    tmpNodes.push(...labels);
    yield* all(
      ...labels.map((label) => label().opacity(1, 1)),
    );

    yield* beginSlide('');
    yield* msg().text('').text('It probably does NOT matter which IDE you choose so long as it supports Jupyter notebooks. Any of the above should give you a comparable experience in 2025.', 1);

    yield* beginSlide('');
    const screenshots = [
      createRef<Img>(),
      createRef<Img>(),
      createRef<Img>(),
    ];
    [
      '../../images/vscode-screenshot.png',
      '../../images/vscode-python-extension.png',
      '../../images/vscode-jupyter-extension.png',
    ].map((src, i) => {
      view.add(
        <Img ref={screenshots[i]} src={src} height={900} margin={20} opacity={0} />
      );
    });
    tmpNodes.push(...screenshots);
    yield* all(
      logos[0]().x(-800, 1),
      labels[0]().x(-800, 1),
      labels[0]().text('Visual\nStudio\nCode\nin 2025', 1),
      ...logos.slice(1).map((logo) => logo().opacity(0, 1)),
      ...labels.slice(1).map((label) => label().opacity(0, 1)),
      msg().opacity(0, 1),
      screenshots[0]().opacity(1, 1),
    );

    yield* beginSlide('');
    yield* footerTxt().text('').opacity(1).text('For VSCode, you will need the Python and Jupyter extensions.', 1);
    const circle = createRef<Circle>();
    view.add(
      <Circle ref={circle} lineWidth={10} stroke={UT_BURNT_ORANGE} startAngle={-180} endAngle={180} zIndex={2} opacity={0} />
    );
    tmpNodes.push(circle);
    circle().x(-579);
    circle().y(-133);
    circle().width(60);
    circle().height(60);
    yield* circle().endAngle(-180).opacity(1).endAngle(180, 0.5);
    yield* waitFor(1);
    yield* all(
      screenshots[0]().opacity(0, 1),
      screenshots[1]().opacity(1, 1),
    );

    yield* beginSlide('');
    yield* all(
      screenshots[1]().opacity(0, 1),
      screenshots[2]().opacity(1, 1),
    );

    yield* beginSlide('');
    yield* all(
      circle().opacity(0, 1),
      screenshots[2]().opacity(0, 1),
      screenshots[0]().opacity(1, 1),
    );
    yield* footerTxt().text('').opacity(1).text('Select your active Python environment.', 1);
    circle().x(430);
    circle().y(360);
    circle().width(230);
    circle().height(55);
    yield* circle().endAngle(-180).opacity(1).endAngle(180, 0.5);
  }

  // -------------------------------------------------------
  // TODO: videos of jupyter notebook actions in VSCode
  { titleStr = 'Jupyter Notebooks';
    footerStr = '[]';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
  }

  // -------------------------------------------------------
  { titleStr = 'Learning Goals';
    footerStr = '[]';
    yield* beginSlide(titleStr);
    // clean up previous slide
    clearNodes(tmpNodes);
    clearLayout(mainLayout());
    // footer there but invisible
    footerTxt().opacity(0).text(footerStr);
    // write title
    yield* titleTxt().text('').text(titleStr, 1);
    // content
    mainLayout().direction('column');
    const bmiImg = createRef<Img>();
    mainLayout().add(
      <Img ref={bmiImg} src={'../../images/logos/brain-machine-interface-logo.png'} height={150} margin={20} opacity={0} />
    );
    const goalsLayout = createRef<Layout>();
    mainLayout().add(
      <Layout ref={goalsLayout} grow={1}  direction={'column'} justifyContent={'start'} alignItems={'start'} padding={40} gap={40}></Layout>
    );
    const goals: Reference<Txt>[] = [];
    for (let i = 0; i < learningGoals.length; i++) {
      goals.push(createRef<Txt>());
      goalsLayout().add(
        <Txt ref={goals[i]} text={learningGoals[i]} fontSize={60} textWrap={true} opacity={0} />
      );
    }
    yield* all(
      bmiImg().opacity(1, 1),
      ...goals.map((goal) => goal().opacity(0.1, 1)),
    );
    yield* goals[0]().opacity(1, 1);

    yield* beginSlide('');
    yield* all(
      goals[0]().opacity(0.1, 1),
      goals[1]().opacity(1, 1),
    );
  }

  // -------------------------------------------------------
  yield* beginSlide('END');

});

function clearNodes(nodes: Reference<Node>[]) {
  while (nodes.length > 0) {
    let node = nodes.pop();
    node().remove();
    node().dispose();
  }
}

function clearLayout(layout: Layout) {
  layout.children().forEach((child) => {
    child.remove();
    child.dispose();
  });
}
