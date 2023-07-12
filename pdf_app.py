import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import base64

st.set_page_config(layout="centered", page_icon="🎓", page_title="Econ 2013 News Analysis Assignment 01")
st.title("Econ 2013 News Analysis Assignment 01")

# ... previous code ...

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")

# ... previous code ...

submit = form.form_submit_button("Generate PDF")

if submit:
    template_file = open("template.html", "r")
    template_content = template_file.read()
    template_file.close()

    if q02_img01 is not None:
        img_data = q02_img01.read()
        encoded_img = base64.b64encode(img_data).decode("utf-8")
        template_content = template_content.replace("{{ q02_img01 }}", encoded_img)

    if q02_img02 is not None:
        img_data = q02_img02.read()
        encoded_img = base64.b64encode(img_data).decode("utf-8")
        template_content = template_content.replace("{{ q02_img02 }}", encoded_img)

    html = template.render(
        student=student,
        q01=q01,
        # ... other variables ...
        template_content=template_content
    )

    pdf = pdfkit.from_string(html, False)

    st.success("Your template successfully generated!")

    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="your_work.pdf",
        mime="application/octet-stream",
    )
