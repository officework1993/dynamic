
import echonet



#change example.cfg to the desired folder to create a loader for custom dataset.


echonet.utils.segmentation.run(modelname="deeplabv3_resnet50",
                                                    save_segmentation=True,
                                                    pretrained=False)