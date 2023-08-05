#!/usr/bin/env python3

from .pyparagraph import TextWrap, parse_arguments

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
        tw.render_image(text_to_wrap, args.image, img=None, margin=args.margin)
    else:
        tw = TextWrap(args=args)
        lines = tw.render_text(text_to_wrap)
        print("\n".join(lines))


if __name__ == "__main__":
    main()
