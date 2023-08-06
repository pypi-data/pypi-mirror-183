

TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nullam vestibulum velit non eros consequat aliquam.
Nullam ut risus venenatis, laoreet libero at, tempus libero.
Suspendisse potenti. Suspendisse vel mauris in metus varius
egestas vel id ipsum. Class aptent taciti sociosqu ad litora
torquent per conubia nostra, per inceptos himenaeos.
Proin sed ligula mi. Donec cursus, lacus vel pharetra
pellentesque, nunc turpis tristique turpis, in commodo
neque est sit amet ante. Fusce pulvinar, dui in vehicula
luctus, tellus lectus hendrerit diam, id ultricies neque
magna sit amet nisl. Fusce at vulputate ligula, eu tempor
felis. Duis quis molestie neque. Etiam venenatis libero non
sollicitudin faucibus. Duis tempor tincidunt felis. Vestibulum
interdum neque in risus mattis, eget tempus lacus ultricies.
Aenean et lectus pharetra, fringilla ex sed, interdum orci.
Maecenas ullamcorper rutrum felis, ac congue ante sagittis eget.
Pellentesque diam dolor, consequat nec sagittis eget, scelerisque
sed mi. Fusce vulputate laoreet dui posuere dapibus. Vivamus
vestibulum consectetur ipsum, vel vestibulum tortor congue et.
Aenean pellentesque fringilla erat, ac pellentesque lorem eleifend
id. Quisque neque velit, gravida in tempus ac, commodo id mi.
Nulla vel porttitor nibh. Sed et magna vitae eros dictum ultricies.
Aenean vestibulum a nunc eu fringilla.
Donec sollicitudin hendrerit gravida.
Etiam faucibus elit nec mi mattis, at pellentesque nibh vestibulum.
Vestibulum non faucibus ante. Proin luctus tempus blandit. Sed blandit
pellentesque nisl ut porttitor. Aliquam nec tristique dui. Maecenas erat
dui, interdum interdum tempus id, efficitur a nibh.
Donec ut ex elementum, bibendum turpis at, rhoncus odio. Pellentesque
mollis interdum volutpat. Suspendisse potenti. Sed a leo convallis, porta
felis id, faucibus augue. Phasellus purus odio, suscipit nec interdum sed,
scelerisque a sapien. Fusce ut varius velit, volutpat posuere mauris. Quisque
gravida risus a elit egestas elementum. Integer cursus sapien sed lacus iaculis malesuada.
Curabitur tincidunt feugiat mauris, ultricies volutpat est mollis vel.
Nullam dignissim orci vitae volutpat sagittis. Pellentesque habitant morbi
tristique senectus et netus et malesuada fames ac turpis egestas. Sed vestibulum
hendrerit scelerisque. Sed venenatis, mi a molestie ullamcorper, nisl nunc ullamcorper mi,
feugiat porttitor tortor dolor at dolor. Aliquam sem magna, fermentum imperdiet malesuada eu,
maximus quis arcu. Curabitur auctor leo lacus, sit amet porta sem fringilla sed. Mauris sed augue
vulputate nulla efficitur fringilla. Etiam vestibulum massa sit amet pretium luctus. Ut porta est
ac sodales finibus. Donec congue facilisis odio id mattis."""

result = [5, 5, 3, 3, 5, 5, 7, 9, 8, 5, 1, 4, 9, 5, 2, 3, 6, 5,
          6, 3, 6, 11, 6, 6, 3, 6, 2, 5, 7, 3, 2, 6, 3, 4, 2, 4,
          2, 8, 3, 7, 7, 3, 8, 8, 3, 4, 3, 5, 3, 5, 3, 7, 2, 6, 5,
          7, 2, 6, 3, 3, 4, 5, 5, 9, 3, 2, 9, 4, 6, 5, 5, 2, 7, 5,
          3, 4, 5, 5, 2, 5, 5, 2, 11, 4, 4, 6, 4, 5, 5, 6, 6, 7, 4,
          6, 3, 6, 8, 3, 2, 3, 5, 2, 6, 5, 10, 2, 6, 5, 5, 2, 4, 8,
          8, 7, 2, 6, 2, 6, 4, 2, 8, 4, 4, 9, 3, 2, 3, 8, 3, 5, 5, 5,
          3, 5, 8, 7, 5, 6, 3, 8, 0, 6, 5, 6, 5, 5, 2, 6, 5, 5, 5, 3,
          6, 5, 2, 6, 3, 2, 2, 7, 3, 2, 5, 3, 2, 3, 5, 4, 6, 10, 8, 1,
          2, 2, 10, 7, 5, 9, 6, 4, 3, 2, 5, 2, 6, 4, 4, 1, 6, 5, 5, 4,
          6, 8, 3, 9, 4, 2, 3, 7, 3, 5, 4, 4, 9, 8, 8, 6, 3, 5, 1, 9,
          2, 2, 5, 6, 6, 3, 7, 3, 9, 8, 7, 6, 6, 3, 1, 3, 8, 11, 3, 6,
          4, 5, 3, 3, 4, 3, 8, 9, 1, 7, 5, 2, 6, 6, 6, 5, 7, 9, 3, 1,
          4, 3, 5, 5, 2, 6, 3, 5, 5, 11, 3, 7, 7, 7, 6, 3, 4, 8, 4, 4,
          5, 6, 3, 6, 4, 8, 4, 2, 5, 2, 6, 5, 2, 6, 4, 3, 9, 7, 3, 6, 2,
          1, 6, 8, 4, 2, 7, 9, 2, 0, 3, 2, 4, 7, 3, 4, 5, 5, 6, 7, 4, 5,
          5, 6, 3, 6, 3, 4, 5, 3, 5, 4, 6, 3, 5, 3, 5, 6, 5, 8, 1, 3, 4,
          7, 5, 2, 5, 6, 5, 6, 5, 6, 4, 2, 2, 5]
