function textToAudio() {
    // var text = '';
    var text = document.getElementById("text_output").textContent;
    cancelAudio();
    let speech = new SpeechSynthesisUtterance();
    // var i;
    // for (i = 0; i < x.length; i++) {
    //     text = text + x[i].textContent;
    // }
    // var voices = speech.getVoices;
    speech.lang = "en-US";
    // speech.voice = voices[1];
    speech.text = text;
    speech.volume = 1;
    speech.rate = 0.7;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}

function pauseAudio() {
    window.speechSynthesis.pause();
}

function resumeAudio() {
    window.speechSynthesis.resume();
}

function cancelAudio() {
    window.speechSynthesis.cancel();
}

// if (annyang) {
//     // Add our commands to annyang
//     annyang.addCommands({
//         'hello': function() {
//             alert('Hello world!');
//         },
//         'start reading': textToAudio,
//         'pause reading': pauseAudio,
//         'resume reading': resumeAudio,
//         'stop reading': cancelAudio,
//     });
//
//     // Start listening. You can call this here, or attach this call to an event, button, etc.
// }
//
// function speakcommand() {
//     annyang.start({
//         autoRestart: false
//     });
// }
