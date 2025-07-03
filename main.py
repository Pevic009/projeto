def on_left_pressed():
    global mySprite
    if True:
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . f f f f f f . . . . .
                    . . . . f 2 f e e e e f f . . .
                    . . . f 2 2 2 f e e e e f f . .
                    . . . f e e e e f f e e e f . .
                    . . f e 2 2 2 2 e e f f f f . .
                    . . f 2 e f f f f 2 2 2 e f . .
                    . . f f f e e e f f f f f f f .
                    . . f e e 4 4 f b e 4 4 e f f .
                    . . f f e d d f 1 4 d 4 e e f .
                    . f d d f d d d d 4 e e e f . .
                    . f b b f e e e 4 e e f . . . .
                    . f b b e d d 4 2 2 2 f . . . .
                    . . f b e d d e 4 4 4 f f . . .
                    . . . f f e e f f f f f f . . .
                    . . . . f f f . . . f f . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . f f f f f f . . . . .
                    . . . . f 2 f e e e e f f . . .
                    . . . f 2 2 2 f e e e e f f . .
                    . . . f e e e e f f e e e f . .
                    . . f e 2 2 2 2 e e f f f f . .
                    . . f 2 e f f f f 2 2 2 e f . .
                    . . f f f e e e f f f f f f f .
                    . . f e e 4 4 f b e 4 4 e f f .
                    . . . f e d d f 1 4 d 4 e e f .
                    . . . . f d d d e e e e e f . .
                    . . . . f e 4 e d d 4 f . . . .
                    . . . . f 2 2 e d d e f . . . .
                    . . . f f 5 5 f e e f f f . . .
                    . . . f f f f f f f f f f . . .
                    . . . . f f f . . . f f . . . .
                    """),
                img("""
                    . . . . . f f f f f f . . . . .
                    . . . . f 2 f e e e e f f . . .
                    . . . f 2 2 2 f e e e e f f . .
                    . . . f e e e e f f e e e f . .
                    . . f e 2 2 2 2 e e f f f f . .
                    . . f 2 e f f f f 2 2 2 e f . .
                    . . f f f e e e f f f f f f f .
                    . . f e e 4 4 f b e 4 4 e f f .
                    . . f f e d d f 1 4 d 4 e e f .
                    . f d d f d d d d 4 e e e f . .
                    . f b b f e e e 4 e e f f . . .
                    . f b b e d d 4 2 2 2 f . . . .
                    . . f b e d d e 2 2 2 e . . . .
                    . . . f f e e f 4 4 4 f . . . .
                    . . . . . f f f f f f . . . . .
                    . . . . . . . f f f . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . f f f f f f . . . . . .
                    . . . f 2 f e e e e f f . . . .
                    . . f 2 2 2 f e e e e f f . . .
                    . . f e e e e f f e e e f . . .
                    . f e 2 2 2 2 e e f f f f . . .
                    . f 2 e f f f f 2 2 2 e f . . .
                    . f f f e e e f f f f f f f . .
                    . f e e 4 4 f b e 4 4 e f f . .
                    . . f e d d f 1 4 d 4 e e f . .
                    . . . f d d d e e e e e f . . .
                    . . . f e 4 e d d 4 f . . . . .
                    . . . f 2 2 e d d e f . . . . .
                    . . f f 5 5 f e e f f f . . . .
                    . . f f f f f f f f f f . . . .
                    . . . f f f . . . f f . . . . .
                    """)],
            500,
            False)
    else:
        mySprite = sprites.create(img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            SpriteKind.player)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)