var edgeObservation = {
    start: function(params, next) {

        params['results'].push(['trial','block','s1','s2','connected','response','accuracy','rt'])

        space = oCanvas.create({
            canvas: edgeObservation.initCanvas(),
            background: 'rgb(208, 213, 219)',
        })

        edgeObservation.initResizeListener()

        cX = space.canvasElement.width / 2
        cY = space.canvasElement.height / 2

        mX = space.canvasElement.width
        mY = space.canvasElement.height

        // event state
        var s = {
            initTime: new Date().getTime(),
            acc_history: [],
            rt: 0,
            last_response: null,
            acc: null,
            trial: 0,
            block: 0,
            state: 'observation',
            finish_early: false,
            block_order: edgeObservation.generateBlockOrder(params['pairs']),
            connection: null,
        }

        s['connection'] = s['block_order'][s['trial']][2]
        elements = edgeObservation.initElements()
        edgeObservation.initStim(
            stimuli.stimLabels[s['block_order'][s['trial']][0]],
            stimuli.stimLabels[s['block_order'][s['trial']][1]],
        )

        observation()
        // ___ Event Logic ___
        function observation() {
            space.scenes.load('observation')
            s['state'] = 'block'
            s['rt'] = new Date().getTime() - s['initTime']

            setTimeout( function () {
                setTimeout( function () {
                    s['state'] = 'continue'
                    space.scenes.load('continue')
                }, 50)
            }, 500)
        }

        function next_trial() {
            space.scenes.unload('continue')

            params['results'].push([s['trial'], s['block'], stimuli.stimLabels[s['block_order'][s['trial']][0]], stimuli.stimLabels[s['block_order'][s['trial']][1]], s['connection'], s['last_response'], s['acc'], s['rt']])
            s['acc_history'].push(s['acc'])

            s['trial'] += 1
            if (s['trial'] >= s['block_order'].length) {
                s['trial'] = 0
                s['block'] += 1
                if (s['block'] >= params['n_blocks']) {
                    edgeObservation.destroySpace()
                    next()
                }
                s['block_order'] = edgeObservation.generateBlockOrder(params['pairs'])
            }

            s['connection'] = s['block_order'][s['trial']][2]

            s1.obj.remove()
            s2.obj.remove()

            setTimeout( function () {
                edgeObservation.initStim(
                    stimuli.stimLabels[s['block_order'][s['trial']][0]],
                    stimuli.stimLabels[s['block_order'][s['trial']][1]],
                )
                space.scenes.load('observation')
                setTimeout( function () {
                    observation()
                    s['state'] = 'observation'
                    s['initTime'] = new Date().getTime()
                }, 1000)
            }, 200)

        }

        // - Bind Actions to Elements -
        elements['continue']['obj'].bind('click tap', function () {
            if (s['state'] == 'continue') {
                s['state'] = 'block'
                next_trial()
            }
        })

        // f = yes (70); j = no (74); space = continue
        space.bind("keydown", function () {
            if (s['state'] == 'continue') {
                // space == continue
                if (space.keyboard.getKeysDown().includes(32) == true) {
                    s['state'] = 'block'
                    next_trial()
                }
            }
        })
    },

    //-----------------------------------------------------v

    initElements: function () {

        elements = {}

        // ___ Phase 1 (Selection) ___
        elements.titleInstructions = {
            obj: space.display.rectangle({
                origin: { x: "center", y: "center" }, align: 'center',
                fill: "rgba(255,255,255,.4)",
                width: 950,
                height: 65,
                // zIndex: "front",
            }),
            setlocation: function() {
                this['obj'].x = cX
                this['obj'].y = 20
            }
        }
        elements.titleInstructions['obj'].addChild(
            space.display.text({
                x: 0,
                y: 10,
                origin: { x: "center", y: "center" }, align: 'center',
                align: "center",
                font: "bold 32px sans-serif",
                text: "Click 'continue' when you have finished studying this pair.",
                fill: "rgba(0,0,0,1)",
                zIndex: "front",
            })
        )

        elements.feedbackTxtBackground = {
            obj: space.display.rectangle({
                origin: { x: "center", y: "center" }, align: 'center',
                fill: "rgba(255,255,255,.8)",
                width: 600,
                height: 80,
            }),
            setlocation: function() {
                this['obj'].x = cX
                this['obj'].y = mY - 140
            }
        }
        elements.feedbackTxt = {
            obj: space.display.text({
                origin: { x: "center", y: "center" }, align: 'center',
                align: "center",
                font: "bold 35px sans-serif",
                text: "These fish can go in the same tank.",
                fill: "rgba(0,0,0,1)",
                zIndex: "front",
            }),
            setlocation: function() {
                this['obj'].x = cX
                this['obj'].y = mY - 140
            }
        }
        elements.feedbackTxtBackground['obj'].addChild(elements.feedbackTxt['obj'])
        space.scenes.create('observation', function () {
            this.add(elements.titleInstructions['obj'])
            this.add(elements.feedbackTxt['obj'])
        })


        // ___ Phase 2 (Continue) ___
        elements.continue = {
            obj: space.display.rectangle({
                origin: { x: "center", y: "center" }, align: 'center',
                height: 90,
                width: 360,
                fill: "rgba(240,240,240)",
                stroke: "4px black",
                join: "round",
            }),
            setlocation: function () {
                this['obj'].x = cX
                this['obj'].y = mY - 50
            }
        }
        elements.continue['obj'].addChild(
            space.display.text({
                x: 0,
                y: 0,
                origin: { x: "center", y: "center" }, align: 'center',
                align: "center",
                font: "bold 35px sans-serif",
                text: "Continue\n(press 'space')",
                fill: "rgba(0,0,0,1)",
                zIndex: "front",
            })
        )

        space.scenes.create('continue', function () {
            this.add(elements.continue['obj'])
        })

        elements_list = [
            elements.titleInstructions,
            elements.feedbackTxt,
            elements.feedbackTxtBackground,
            elements.continue,
        ]

        for (let i of [...Array(elements_list.length).keys()]) {
            elements_list[i].setlocation()
        }

        return elements
    },

    //-----------------------------------------------------v

    initStim: function (s1id, s2id) {

        s1 = {
            obj: space.display.image({
                image: s1id,
                origin: { x: "center", y: "center" },
            }),

            setlocation: function() {
                this.obj.x = cX
                this.obj.y = cY - 100 - 50
            }
        }
        s1.setlocation()

        s2 = {
            obj: space.display.image({
                image: s2id,
                origin: { x: "center", y: "center" },
            }),

            setlocation: function() {
                this.obj.x = cX
                this.obj.y = cY + 100 - 50
            }
        }
        s2.setlocation()


        space.addChild(s1.obj)
        space.addChild(s2.obj)

    },

    //-----------------------------------------------------v

    initCanvas: function () {
        canvas = document.createElement('canvas', {id: 'canvas', style: 'position:absolute;'})
        document.getElementById('main').appendChild(canvas)

        var ctx = canvas.getContext('2d');
        // ctx.lineWidth = 2;

        ctx.canvas.width  = window.innerWidth - 20;
        ctx.canvas.height = window.innerHeight - 20;

        return canvas
    },

    //-----------------------------------------------------v

    generateBlockOrder: function (objects) {
        let block = []
        idx = [...Array(objects.length).keys()] // from ben @ https://stackoverflow.com/a/10050831
        idx = edgeObservation.shuffle(idx)

        for (let i of idx) {
            block.push([
                ...edgeObservation.shuffle([objects[i][0], objects[i][1]]),
                objects[i][2]
            ])
        }

        return block
    },

    //----------------------------------------------------v

    shuffle: function (array) { // from mike bostok @ https://bost.ocks.org/mike/shuffle/
        var m = array.length, t, i;

        // While there remain elements to shuffle…
        while (m) {

            // Pick a remaining element…
            i = Math.floor(Math.random() * m--);

            // And swap it with the current element.
            t = array[m];
            array[m] = array[i];
            array[i] = t;
        }

        return array;

    },

    //----------------------------------------------------v

    initResizeListener: function () {
        window.addEventListener('resize', function () {
            space.width = window.innerWidth - 20;
            space.height = window.innerHeight - 20;

            cX = space.canvasElement.width / 2
            cY = space.canvasElement.height / 2

            mX = space.canvasElement.width
            mY = space.canvasElement.height

            for (let i of [...Array(elements_list.length).keys()]) {
                elements_list[i].setlocation()
            }
            s1.setlocation()
            s2.setlocation()
        }, false);
    },

    //----------------------------------------------------v

    mean: function(numbers) {
        return edgeObservation.sum(numbers) / numbers.length;
    },

    sum: function(numbers) {
        var total = 0;
        for(var i = 0; i < numbers.length; i++) {
            total += numbers[i];
        }
        return total;
    },

    //----------------------------------------------------v

    destroySpace: function () {
        space.destroy(space)
        document.getElementById('main').innerHTML = ''
    },
}
