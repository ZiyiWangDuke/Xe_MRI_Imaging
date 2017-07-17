import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# imslice function for 3D image visualization
def imslice(imData):
    # play with plot tool
    f1 = plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
    ax = f1.add_subplot(111)
    ax.axis('off')

    # create slider
    axColor = 'skyblue'
    axSlice = plt.axes([0.15, 0.03, 0.65, 0.03], facecolor=axColor)

    sliceSlider = Slider(axSlice, 'Slice', 0, imData.shape[0], valinit=0, valfmt='%d')
    sliceSlider.label.set_fontsize(20)

    # create radio button
    rax = plt.axes([0.88, 0.03, 0.10, 0.15], facecolor=axColor)
    radio = RadioButtons(rax, ('Dim 1', 'Dim 2', 'Dim 3'))

    # update image from slider and radio button
    def update(val):
        t = sliceSlider.val
        dim = radio.value_selected
        current = int(t)

        def one(): ax.imshow(imData[current, :, :], cmap='Greys')
        def two():  ax.imshow(imData[:, current, :], cmap='Greys')
        def three():  ax.imshow(imData[:, :, current], cmap='Greys')

        option = {'Dim 1':one, 'Dim 2':two, 'Dim 3':three}
        y = option[dim]()

    sliceSlider.on_changed(update)
    radio.on_clicked(update)

    plt.show()