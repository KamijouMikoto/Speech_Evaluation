import os

from airium import Airium


SELF_EVALUATION_QUESTIONS = [
    "I am an empathic person, e.g. I get sad or angry during dramatic scenes in movies.",
    "I can easily hear and identify how a person feels in a phone conversation. I don’t need to see them to recognize their emotions.",
    "I am musically trained, e.g. I can play a musical instrument.",
    "High audio quality in media is important to me, e.g. I own high-end speakers.",
    "I am good at predicting other people’s behavior , e.g. I know how my actions will make others feel."
]


def get_file_list():
    return sorted(os.listdir('./out/samples'))


def generate_html():
    a = Airium()

    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.title(_t="Speech Evaluation")
            a.meta(name="viewport", content="width=device-width, initial-scale=1.0")
            a.link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6", crossorigin="anonymous")
        with a.body():
            with a.div(klass="container pb-5 pt-5"):
                a.h1(_t="Emotional Speech Evaluation", klass="text-center text-success display-1 pt-5 pb-5")
                a.p(
                    _t="Thank you for your time and welcome to the subjective evaluation of our emotional speech samples!",
                    klass="pt-5"
                )
                a.p(
                    _t="""First, you will need to answer 5 questions about yourself to make us know you more.
                    Then you will hear overall 80 audio samples, for each of which you are invited to answer 5 questions.
                    If you are uncertain about an answer listen to the audio sample multiple times.
                    """
                )
                a.p(
                    _t="""It is highly recommended to wear headphones during the evaluation.
                    """
                )
                with a.p():
                    a.span(_t="""After you click ‘Submit’, all your answers will be recorded, and a CSV file will be
                    downloaded. Please send the CSV file to 
                    """)
                    a.a(
                        href="mailto:zijiang.yang@informatik.uni-augsburg.de?subject=Emotional Speech Evalution",
                        _t="zijiang.yang@informatik.uni-augsburg.de",
                        target="_blank",
                        rel="noopener noreferrer"
                    )
                    a.span(
                        _t=". Thanks for your help!"
                    )
                a.p(_t="Note: Please answer all questions. ‘Submit’ button will bring you back to the unfinished questions.")
                a.p(_t="When answering questions related to emotions please consider the following definitions:")
                with a.ul():
                    with a.li():
                        a.span(_t="Please select ")
                        a.strong(_t="‘Neutral’")
                        a.span(_t=" if you think the speaker does not express a particular emotion.")
                    with a.li():
                        a.span(_t="Please select ")
                        a.strong(_t="‘Anger’")
                        a.span(_t=" if you think the speaker is mad or furious about something.")
                    with a.li():
                        a.span(_t="Please select ")
                        a.strong(_t="‘Amused’")
                        a.span(_t=" if you think the speaker finds something funny or interesting.")
                    with a.li():
                        a.span(_t="Please select ")
                        a.strong(_t="‘Disgust’")
                        a.span(_t=" if you think the speaker feels nauseating or disgusted.")
                    with a.li():
                        a.span(_t="Please select ")
                        a.strong(_t="‘Sleepy’")
                        a.span(_t=" if you think the speaker is tired or exhausted.")
                with a.form(klass="pt-5 pb-5", id="evaluation-form", action="#", onsubmit="return submitForm();"):
                    with a.div(klass="form-group col-md-4"):
                        a.label(_t="Name", for_="name-input")
                        a.input(id="name-input", klass="form-control", type="text", placeholder="Jane Smith", required=True)
                    with a.div(klass="form-group col-md-8"):
                        for index, question in enumerate(SELF_EVALUATION_QUESTIONS):
                            with a.div(klass="card mt-5"):
                                with a.div(klass="card-body"):
                                    a.p(_t=question, klass="pb-3")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-1", name=f"self-evaluation-{index}", klass="custom-control-input", value=1, required=True)
                                        a.label(_t="1 — Strongly disagree", klass="custom-control-label", for_=f"self-evaluation-{index}-1")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-2", name=f"self-evaluation-{index}", klass="custom-control-input", value=2)
                                        a.label(_t="2 — Disagree", klass="custom-control-label", for_=f"self-evaluation-{index}-2")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-3", name=f"self-evaluation-{index}", klass="custom-control-input", value=3)
                                        a.label(_t="3 — Neutral", klass="custom-control-label", name=f"self-evaluation-{index}", for_=f"self-evaluation-{index}-3")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-4", name=f"self-evaluation-{index}", klass="custom-control-input", value=4)
                                        a.label(_t="4 — Agree", klass="custom-control-label", for_=f"self-evaluation-{index}-4")
                                    with a.div(klass="custom-control custom-radio form-check-inline"):
                                        a.input(type="radio", id=f"self-evaluation-{index}-5", name=f"self-evaluation-{index}", klass="custom-control-input", value=5)
                                        a.label(_t="5 — Strongly agree", klass="custom-control-label", for_=f"self-evaluation-{index}-5")
                    a.h4(_t="Emotional Speech Evalution", klass="mt-5 pt-5 text-success")
                    for index, file in enumerate(get_file_list()):
                        if index % 2 == 1:
                            color_scheme = "bg-secondary bg-gradient text-white"
                        else:
                            color_scheme = "bg-light bg-gradient"
                        with a.div(klass=f"card mt-5 {color_scheme}"):
                            with a.div(klass="card-body"):
                                with a.div(klass="row"):
                                    with a.div(klass="col-lg-4 align-self-center"):
                                        with a.div(klass="text-center"):
                                            a.h6(_t=f"Sample {index + 1}")
                                            a.audio(controls=True, src=f"samples/{file}", klass='mb-5 mt-5')
                                    with a.div(klass="col-lg-8"):
                                        with a.p(klass="pb-1"):
                                            a.strong(_t="What emotion")
                                            a.span(_t=" do you think of the voice expressed?")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-1-1-{file}", name=f"tts-evaluation-1-{file}", klass="custom-control-input", value=1, required=True)
                                            a.label(_t="1 — Neutral", klass="custom-control-label", for_=f"tts-evaluation-1-1-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-1-2-{file}", name=f"tts-evaluation-1-{file}", klass="custom-control-input", value=2)
                                            a.label(_t="2 — Amused", klass="custom-control-label", for_=f"tts-evaluation-1-2-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-1-3-{file}", name=f"tts-evaluation-1-{file}", klass="custom-control-input", value=3)
                                            a.label(_t="3 — Anger", klass="custom-control-label", for_=f"tts-evaluation-1-3-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-1-4-{file}", name=f"tts-evaluation-1-{file}", klass="custom-control-input", value=4)
                                            a.label(_t="4 — Disgust", klass="custom-control-label", for_=f"tts-evaluation-1-4-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-1-5-{file}", name=f"tts-evaluation-1-{file}", klass="custom-control-input", value=5)
                                            a.label(_t="5 — Sleepy", klass="custom-control-label", for_=f"tts-evaluation-1-5-{file}")
                                        
                                        with a.p(klass="pb-1 pt-5"):
                                            a.span(_t="If ")
                                            a.strong(_t="NOT neutral")
                                            a.span(_t=", what do you think of the ")
                                            a.strong(_t="intensity")
                                            a.span(_t=" of the emotion expressed? (If neutral, please skip this question)")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-2-1-{file}", name=f"tts-evaluation-2-{file}", klass="custom-control-input", value=1, required=True)
                                            a.label(_t="1 — Very weak", klass="custom-control-label", for_=f"tts-evaluation-2-1-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-2-2-{file}", name=f"tts-evaluation-2-{file}", klass="custom-control-input", value=2)
                                            a.label(_t="2 — Weak", klass="custom-control-label", for_=f"tts-evaluation-2-2-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-2-3-{file}",  name=f"tts-evaluation-2-{file}", klass="custom-control-input", value=3, checked=True)
                                            a.label(_t="3 — Moderate", klass="custom-control-label", for_=f"tts-evaluation-2-3-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-2-4-{file}", name=f"tts-evaluation-2-{file}", klass="custom-control-input", value=4)
                                            a.label(_t="4 — Strong", klass="custom-control-label", for_=f"tts-evaluation-2-4-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-2-5-{file}", name=f"tts-evaluation-2-{file}", klass="custom-control-input", value=5)
                                            a.label(_t="5 — Very strong", klass="custom-control-label", for_=f"tts-evaluation-2-5-{file}")

                                        with a.p(klass="pb-1 pt-5"):
                                            a.strong(_t="How close to human")
                                            a.span(_t=" would you rate the voice speaking?")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-3-1-{file}", name=f"tts-evaluation-3-{file}", klass="custom-control-input", value=1, required=True)
                                            a.label(_t="1 — Not at all", klass="custom-control-label", for_=f"tts-evaluation-3-1-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-3-2-{file}", name=f"tts-evaluation-3-{file}", klass="custom-control-input", value=2)
                                            a.label(_t="2 — A little bit close", klass="custom-control-label", for_=f"tts-evaluation-3-2-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-3-3-{file}", name=f"tts-evaluation-3-{file}", klass="custom-control-input", value=3)
                                            a.label(_t="3 — Close", klass="custom-control-label", for_=f"tts-evaluation-3-3-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-3-4-{file}", name=f"tts-evaluation-3-{file}", klass="custom-control-input", value=4)
                                            a.label(_t="4 — Very close", klass="custom-control-label", for_=f"tts-evaluation-3-4-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-3-5-{file}", name=f"tts-evaluation-3-{file}", klass="custom-control-input", value=5)
                                            a.label(_t="5 — Extremely close", klass="custom-control-label", for_=f"tts-evaluation-3-5-{file}")

                                        with a.p(klass="pb-1 pt-5"):
                                            a.span(_t="Do you think the voice is ")
                                            a.strong(_t="clear and understandable")
                                            a.span(_t="?")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-4-1-{file}", name=f"tts-evaluation-4-{file}", klass="custom-control-input", value=1, required=True)
                                            a.label(_t="1 — Strongly disagree", klass="custom-control-label", for_=f"tts-evaluation-4-1-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-4-2-{file}", name=f"tts-evaluation-4-{file}", klass="custom-control-input", value=2)
                                            a.label(_t="2 — Disagree", klass="custom-control-label", for_=f"tts-evaluation-4-2-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-4-3-{file}", name=f"tts-evaluation-4-{file}", klass="custom-control-input", value=3)
                                            a.label(_t="3 — Neutral", klass="custom-control-label", for_=f"tts-evaluation-4-3-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-4-4-{file}", name=f"tts-evaluation-4-{file}", klass="custom-control-input", value=4)
                                            a.label(_t="4 — Agree", klass="custom-control-label", for_=f"tts-evaluation-4-4-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-4-5-{file}", name=f"tts-evaluation-4-{file}", klass="custom-control-input", value=5)
                                            a.label(_t="5 — Strongly agree", klass="custom-control-label", for_=f"tts-evaluation-4-5-{file}")

                                        with a.p(klass="pb-1 pt-5"):
                                            a.span(_t="How much do you ")
                                            a.strong(_t="like")
                                            a.span(_t=" the voice speaking?")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-5-1-{file}", name=f"tts-evaluation-5-{file}", klass="custom-control-input", value=1, required=True)
                                            a.label(_t="1 — Not at all", klass="custom-control-label", for_=f"tts-evaluation-5-1-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-5-2-{file}", name=f"tts-evaluation-5-{file}", klass="custom-control-input", value=2)
                                            a.label(_t="2 — Hardly", klass="custom-control-label", for_=f"tts-evaluation-5-2-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-5-3-{file}", name=f"tts-evaluation-5-{file}", klass="custom-control-input", value=3)
                                            a.label(_t="3 — Moderately", klass="custom-control-label", for_=f"tts-evaluation-5-3-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-5-4-{file}", name=f"tts-evaluation-5-{file}", klass="custom-control-input", value=4)
                                            a.label(_t="4 — Greatly", klass="custom-control-label", for_=f"tts-evaluation-5-4-{file}")
                                        with a.div(klass="custom-control custom-radio form-check-inline"):
                                            a.input(type="radio", id=f"tts-evaluation-5-5-{file}", name=f"tts-evaluation-5-{file}", klass="custom-control-input", value=5)
                                            a.label(_t="5 — Extremely", klass="custom-control-label", for_=f"tts-evaluation-5-5-{file}")
                    with a.div(klass="from-group mt-5"):
                        a.label(_for="open-comments", _t="Please leave your general opinion about the speeches here. We are also happy to hear your valuable suggestions. Thanks!")
                        a.textarea(klass="form-control", id="open-comments", name="open-comments", placeholder="(Optional)", rows="3")
                    a.button(_t="Submit", type="submit", klass="btn btn-primary mt-5")
                    with a.p(klass="mt-3"):
                        a.span(_t="Please send the generated CSV file to ")
                        a.a(
                            href="mailto:zijiang.yang@informatik.uni-augsburg.de?subject=Emotional Speech Evalution",
                            _t="zijiang.yang@informatik.uni-augsburg.de",
                            target="_blank",
                            rel="noopener noreferrer"
                        )
                        a.span(
                            _t=". Thanks for your help!"
                        )
        with a.script():
            a(
                f'''
                function clearForm() {{
                    document.getElementById("evaluation-form").reset();
                }}

                function buildCsvRow(fileName, questionResponses) {{
                    return `${{fileName}};${{questionResponses[0]}};${{questionResponses[1]}};${{questionResponses[2]}};${{questionResponses[3]}};${{questionResponses[4]}}\\n`
                }}

                function getQuestionResponse(input_name) {{
                    return $(`input[name="${{input_name}}"]:checked`).val();
                }}

                function getSelfEvaluationResponses() {{
                    return [{",".join([f"getQuestionResponse('self-evaluation-{index}')" for index in range(5)])}];
                }}

                function getTtsEvaluationResponsesForFile(file_name) {{
                    return [{",".join([f"getQuestionResponse(`tts-evaluation-{index}-${{file_name}}`)" for index in range(1, 6)])}];
                }}

                function getOpenComments() {{
                    let comments = $(`textarea[name="open-comments"]`).val();
                    if ("" === comments) {{
                        return "(Optional)\\n";
                    }} else {{
                        return comments.replace(/\\r?\\n|\\r/g, " ") + "\\n";
                    }}
                }}

                function submitForm() {{
                    let name = $("#name-input").val();
                    let files = [{",".join([f"'{file}'" for file in get_file_list()])}];
                    let csv = "data:text/csv;charset=utf-8,";
                    csv += "filename;q1;q2;q3;q4;q5\\n";
                    csv += buildCsvRow("self_evaluation", getSelfEvaluationResponses());
                    for (let i = 0; i < files.length; i++) {{
                        csv += buildCsvRow(files[i], getTtsEvaluationResponsesForFile(files[i]));
                    }}
                    csv += getOpenComments();
                    let encodedUri = encodeURI(csv);
                    let downloadLink = document.createElement("a");
                    downloadLink.setAttribute("download", `${{name}}_results.csv`);
                    downloadLink.setAttribute("href", encodedUri);
                    document.body.appendChild(downloadLink);
                    downloadLink.click();
                    downloadLink.remove();
                    return false;
                }}
                '''
            )
        a.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js", integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf", crossorigin="anonymous")
        a.script(src="https://code.jquery.com/jquery-3.6.0.min.js", integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=", crossorigin="anonymous")

    return str(a)


if __name__ == '__main__':
    html = generate_html()
    with open('./out/index.html', 'w') as file:
        file.write(html)
