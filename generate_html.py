import os

from collections import defaultdict

from airium import Airium


def get_file_list():
    file_list = os.listdir('./out/samples')

    _files_by_original_file = defaultdict(list)
    
    for file in file_list:
        _files_by_original_file[extract_original_file_name(file)].append(file)

    files_by_original_file = {}
    for original_file, emotional_files in _files_by_original_file.items():

        cycle_gan_files = sorted([file for file in emotional_files if 'cyc' in file])
        vaw_gan_files = sorted([file for file in emotional_files if 'vaw' in file])

        files_by_original_file[original_file] = list(zip(cycle_gan_files, vaw_gan_files))
    return files_by_original_file


def extract_emotion_from_file_name(file_name):
    emotions = {
        'amu': 'Amused',
        'ang': 'Anger',
        'dis': 'Disgust',
        'sle': 'Sleepy'
    }
    return emotions[file_name.split('_')[1]]


def extract_original_file_name(file_name):
    return file_name.split('_')[0]


def emotion_radio_id_from_file_name(file_name):
    return file_name + '-emotionRadio'


def quality_radio_id_from_file_name(file_name):
    return file_name + '-qualityRadio'


def emotion_radio_name_from_file_name(file_name):
    return '_'.join(file_name.split('_')[:2]) + '-emotionRadio'


def quality_radio_name_from_file_name(file_name):
    return '_'.join(file_name.split('_')[:2]) + '-qualityRadio'


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
                a.h1(_t="Speech Evaluation", klass="text-center display-1 pt-5 pb-5")
                with a.form(klass="pt-5 pb-5", id="evaluation-form", action="#", onsubmit="return submitForm();"):
                    with a.div(klass="form-group col-md-4 pt-5 pb-5"):
                        a.label(_t="Name", for_="name-input")
                        a.input(id="name-input", klass="form-control", type="text", placeholder="Jane Smith", required=True)
                    for original_file_name, emotional_files in get_file_list().items():
                        a.h4(_t=original_file_name, klass="pt-5 text-success")
                        for cycle_gan_file, vaw_gan_file in emotional_files:
                            with a.div(klass="row pt-3"):
                                with a.div(klass="form-group col-md-6"):
                                    with a.div(klass="card"):
                                        with a.div(klass="card-body text-center"):
                                            a.h5(_t=f"CycleGAN: {extract_emotion_from_file_name(cycle_gan_file)}", klass="card-title")
                                            a.audio(controls=True, src=f"samples/{cycle_gan_file}")
                                            with a.div(klass="custom-control custom-radio"):
                                                a.input(type="radio", id=emotion_radio_id_from_file_name(cycle_gan_file), name=emotion_radio_name_from_file_name(cycle_gan_file), klass="custom-control-input", value=cycle_gan_file, checked=True)
                                                a.label(_t="This emotion is better.", klass="custom-control-label", for_=emotion_radio_id_from_file_name(cycle_gan_file))
                                            with a.div(klass="custom-control custom-radio"):
                                                a.input(type="radio", id=quality_radio_id_from_file_name(cycle_gan_file), name=quality_radio_name_from_file_name(cycle_gan_file), klass="custom-control-input", value=cycle_gan_file, checked=True)
                                                a.label(_t="This has better speech quality.", klass="custom-control-label", for_=quality_radio_id_from_file_name(cycle_gan_file))
                                with a.div(klass="form-group col-md-6"):
                                    with a.div(klass="card"):
                                        with a.div(klass="card-body text-center"):
                                            a.h5(_t=f"VAW-GAN: {extract_emotion_from_file_name(vaw_gan_file)}", klass="card-title")
                                            a.audio(controls=True, src=f"samples/{vaw_gan_file}")
                                            with a.div(klass="custom-control custom-radio"):
                                                a.input(type="radio", id=emotion_radio_id_from_file_name(vaw_gan_file), name=emotion_radio_name_from_file_name(vaw_gan_file), klass="custom-control-input", value=vaw_gan_file)
                                                a.label(_t="That emotion is better.", klass="custom-control-label", for_=emotion_radio_id_from_file_name(vaw_gan_file))
                                            with a.div(klass="custom-control custom-radio"):
                                                a.input(type="radio", id=quality_radio_id_from_file_name(vaw_gan_file), name=quality_radio_name_from_file_name(vaw_gan_file), klass="custom-control-input", value=vaw_gan_file)
                                                a.label(_t="That has better speech quality.", klass="custom-control-label", for_=quality_radio_id_from_file_name(vaw_gan_file))
                    a.button(_t="Download CSV", type="submit", klass="btn btn-primary mt-5")
        with a.script():
            a(
                f'''
                function clearForm() {{
                    document.getElementById("evaluation-form").reset();
                }}

                function buildCsvRow(emotionFile, qualityFile, firstModel, secondModel) {{
                    let fileNameParts = emotionFile.split("_")
                    return `${{fileNameParts[0]}};${{fileNameParts[1]}};${{emotionFile.includes(firstModel) ? 0 : 1}};${{qualityFile.includes(firstModel) ? 0 : 1}}\\n`
                }}

                function getEmotionRadioData() {{
                    return [
                        {','.join([
                            f'$("input[name={emotion_radio_name_from_file_name(model_files[0])}]:checked").val()'
                            for _, model_file_list in get_file_list().items()
                            for model_files in model_file_list
                        ])}
                    ]
                }}

                function getQualityRadioData() {{
                    return [
                        {','.join([
                            f'$("input[name={quality_radio_name_from_file_name(model_files[0])}]:checked").val()'
                            for _, model_file_list in get_file_list().items()
                            for model_files in model_file_list
                        ])}
                    ]
                }}

                function submitForm() {{
                    const FIRST_MODEL = "cyc";
                    const SECOND_MODEL = "vaw";
                    
                    let name = $("#name-input").val();
                    let emotionRadioData = getEmotionRadioData()
                    let qualityRadioData = getQualityRadioData()

                    let csv = "data:text/csv;charset=utf-8,";

                    csv += "filename;emotion;expression;quality\\n"

                    for (let i = 0; i < emotionRadioData.length; i++) {{
                        csv += buildCsvRow(emotionRadioData[i], qualityRadioData[i], FIRST_MODEL, SECOND_MODEL);
                    }}

                    let encodedUri = encodeURI(csv);

                    let downloadLink = document.createElement("a");
                    downloadLink.setAttribute("download", `${{name}}_${{FIRST_MODEL}}_${{SECOND_MODEL}}.csv`);
                    downloadLink.setAttribute("href", encodedUri);
                    document.body.appendChild(downloadLink);
                    downloadLink.click();
                    downloadLink.remove();

                    clearForm();
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
