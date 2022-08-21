var stimuli = {

    startingInstructions: {
        'class': "<p style='font-size: 18px;'>\
                Hi! Thanks for participating.\
                <br><br>\
                In this experiment you will be shown pairs of fish. On each trial, your task is to judge whether or not the two fish should go in the same tank \
                <br><br>\
                You will be given feedback on each trial indicating whether your guess was correct or incorrect.\
                <br><br>\
                Afterwards, there will be a test phase to see how well you learned.\
                <br><br>\
                Good Luck!\
                <br><br>\
                Click the 'Next' button to begin the experiment.\
            <p>"
        ,
        'obs': "<p style='font-size: 18px;'>\
                Hi! Thanks for participating.\
                <br><br>\
                In this experiment you will be shown pairs of fish. Specifically, each pair of fish that you are shown will go well together in a tank. \
                <br><br>\
                Each trial will be an opportunity to learn what makes 2 fish good partners in a fish tank. \
                <br><br>\
                Afterwards, there will be a test phase to see how well you learned.\
                <br><br>\
                Good Luck!\
                <br><br>\
                Click the 'Next' button to begin the experiment.\
            <p>"
        ,
    },

    generalizationPhaseInstructions: "\
        <p style='font-size: 18px;'>\
            Nice work! Thanks for completing that phase of the experiment. \
            <br><br>\
            In the next phase, you will again be shown pairs of fish. Your task is to decide if they should go in the same tank.\
            <br><br>\
            This time, you will not receive feedback.\
            <br><br>\
            Good Luck!\
            <br><br>\
            Click the 'Next' button to begin the experiment. \
            <br><br>\
        <p>\
    ",

    exitInstructions: "<p style='font-size: 18px;'>\
            That's all. Thanks for participating in this phase of the study. \
            <br><br> \
            Click the 'Next' button to move on to the next phase.\
        <p>"
    ,

    stimLabels: [
        './static/experiments/de1b/materials/stim_files/1.png',
        './static/experiments/de1b/materials/stim_files/2.png',
        './static/experiments/de1b/materials/stim_files/3.png',
        './static/experiments/de1b/materials/stim_files/4.png',
        './static/experiments/de1b/materials/stim_files/5.png',
        './static/experiments/de1b/materials/stim_files/6.png',
        './static/experiments/de1b/materials/stim_files/7.png',
        './static/experiments/de1b/materials/stim_files/8.png',
        './static/experiments/de1b/materials/stim_files/9.png',
        './static/experiments/de1b/materials/stim_files/10.png',
        './static/experiments/de1b/materials/stim_files/11.png',
        './static/experiments/de1b/materials/stim_files/12.png',
        './static/experiments/de1b/materials/stim_files/13.png',
        './static/experiments/de1b/materials/stim_files/14.png',
        './static/experiments/de1b/materials/stim_files/15.png',
        './static/experiments/de1b/materials/stim_files/16.png',
    ],

    possibleGeneralziations: {
        0: [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],
        1: [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9], [9, 8], [9, 10], [10, 9], [10, 11], [11, 10], [11, 12], [12, 11], [12, 13], [13, 12], [13, 14], [14, 13], [14, 15], [15, 14]],
        2: [[0, 2], [1, 3], [2, 0], [2, 4], [3, 1], [3, 5], [4, 2], [4, 6], [5, 3], [5, 7], [6, 4], [6, 8], [7, 5], [7, 9], [8, 6], [8, 10], [9, 7], [9, 11], [10, 8], [10, 12], [11, 9], [11, 13], [12, 10], [12, 14], [13, 11], [13, 15], [14, 12], [15, 13]],
        3: [[0, 3], [1, 4], [2, 5], [3, 0], [3, 6], [4, 1], [4, 7], [5, 2], [5, 8], [6, 3], [6, 9], [7, 4], [7, 10], [8, 5], [8, 11], [9, 6], [9, 12], [10, 7], [10, 13], [11, 8], [11, 14], [12, 9], [12, 15], [13, 10], [14, 11], [15, 12]],
        4: [[0, 4], [1, 5], [2, 6], [3, 7], [4, 0], [4, 8], [5, 1], [5, 9], [6, 2], [6, 10], [7, 3], [7, 11], [8, 4], [8, 12], [9, 5], [9, 13], [10, 6], [10, 14], [11, 7], [11, 15], [12, 8], [13, 9], [14, 10], [15, 11]],
        5: [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 0], [5, 10], [6, 1], [6, 11], [7, 2], [7, 12], [8, 3], [8, 13], [9, 4], [9, 14], [10, 5], [10, 15], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10]],
        6: [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [6, 12], [7, 1], [7, 13], [8, 2], [8, 14], [9, 3], [9, 15], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9]],
        7: [[0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 0], [7, 14], [8, 1], [8, 15], [9, 2], [10, 3], [11, 4], [12, 5], [13, 6], [14, 7], [15, 8]],
        8: [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [8, 0], [9, 1], [10, 2], [11, 3], [12, 4], [13, 5], [14, 6], [15, 7]],
        9: [[0, 9], [1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [9, 0], [10, 1], [11, 2], [12, 3], [13, 4], [14, 5], [15, 6]],
        10: [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [10, 0], [11, 1], [12, 2], [13, 3], [14, 4], [15, 5]],
        11: [[0, 11], [1, 12], [2, 13], [3, 14], [4, 15], [11, 0], [12, 1], [13, 2], [14, 3], [15, 4]],
        12: [[0, 12], [1, 13], [2, 14], [3, 15], [12, 0], [13, 1], [14, 2], [15, 3]],
        13: [[0, 13], [1, 14], [2, 15], [13, 0], [14, 1], [15, 2]],
        14: [[0, 14], [1, 15], [14, 0], [15, 1]],
        15: [[0, 15], [15, 0]]
    },

    generatePairs: function () {


        obs1 = [ // 16
            [0, 8],
            [1, 9],
            [2, 10],
            [3, 11],
            // [4, 12],
            // [5, 13],
            // [6, 14],
            // [7, 15],
            [8, 0],
            [9, 1],
            [10, 2],
            [11, 3],
            // [12, 4],
            // [13, 5],
            // [14, 6],
            // [15, 7],
        ]

        obs2 = [ // 15
            [ 0,  1],
            [ 1,  2],
            [ 2,  3],
            [ 3,  4],
            [ 4,  5],
            [ 5,  6],
            [ 6,  7],
            // [ 7,  8],
            // [ 8,  9],
            // [ 9, 10],
            // [10, 11],
            // [11, 12],
            // [12, 13],
            // [13, 14],
            // [14, 15],
        ]

        obs3 = [ // 15
            [ 0,  0],
            [ 1,  1],
            [ 2,  2],
            [ 3,  3],
            [ 4,  4],
            [ 5,  5],
            [ 6,  6],
            [ 7,  7],
            // [ 8,  8],
            // [ 9,  9],
            // [10, 10],
            // [11, 11],
            // [12, 12],
            // [13, 13],
            // [14, 14],
            // [15, 15],
        ]



        var highGens = {}

        // build high generalization range
        for (let diff in stimuli.possibleGeneralziations) {
            highGens[diff] = []
            for (let pair in stimuli.possibleGeneralziations[diff]) {
                sum = stimuli.possibleGeneralziations[diff][pair].reduce(function (a, b) {
                  return a + b;
                }, 0)
                if (sum >= 16) {
                    highGens[diff].push(stimuli.possibleGeneralziations[diff][pair])
                }
            }
        }        

        console.log(highGens)

        var generalization = []

        // randomly sample 2 items from each possible stim difference
        for (var i of [...Array(16).keys()]) {
            for (var idx of stimuli.shuffle(highGens[i]).slice(0,2) ) {
                generalization.push([...idx, 2])
            }
        }

        return {
            obs1: obs1,
            obs2: obs2,
            obs3: obs3,
            generalization: generalization,
        }

    },

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
}