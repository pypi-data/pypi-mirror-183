#!/usr/bin/env python3

import copy

from .pyparagraph import TextWrap, parse_arguments

desc_sample = "But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. The brave men, <b>living and dead</b>, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a <i>new birth of freedom</i>—and that government of the people, by the people, for the people, shall not perish from the earth."

def main():

    args = parse_arguments()

    if args.test:
        test_args = copy.copy(args)
        test_args.image = False
        tw = TextWrap(args=test_args)
        lines = tw.render_text(desc_sample)
        for line in lines:
            print(line)

    if args.test:
        text_to_wrap = desc_sample
    else:
        text_to_wrap = open(args.file, "r").read()

    if args.image:
        tw = TextWrap(args=args)
        tw.render_image_to_file(text_to_wrap, args.image, margin=args.margin)
    else:
        tw = TextWrap(args=args)
        lines = tw.render_text(text_to_wrap)
        print("\n".join(lines))


if __name__ == "__main__":
    main()
