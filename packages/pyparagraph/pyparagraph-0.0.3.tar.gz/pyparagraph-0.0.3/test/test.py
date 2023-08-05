from pyparagraph import TextWrap

args = {
    "font": "Lato",
    "font-size": "24px",
    "width": "600"
}

text = """Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this."""

# Render to a file of the given name
textwrap = TextWrap.text_wrapper(args)
textwrap.render_image(text, filename="gettysburg.png", margin=20)


# Render to a PIL Image:

from PIL import Image
mine = Image.new("RGBA", (800,800), "white")

textwrap.render_image(text, img=mine)
mine.save("gettysburg2.png")
