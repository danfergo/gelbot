from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC

from worlds.components.g01_finger import GFinger


@interface()
class GHandInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-hand',
    components=[
        GFinger
    ],
    defaults={
        'mjc_interface': GHandInterfaceMJC
    },
    # language=xml
    template="""
        <mujoco>
            <worldbody>
                <body pos='0 0.01 0.025'>
                    <body pos='-0.03 0 0.06'>
                        <g-finger name='finger1'/>    
                    </body>
                    <body pos='0 0 0.06'>
                        <g-finger name='finger2'/>    
                    </body>
                    <body pos='0.04 0 0.02'>
                        <g-finger name='finger3'/>    
                    </body>
                </body>
                
                <body pos='0 0 0.02'>
                    <geom type='box' size='0.02 0.008 0.04' pos='-0.02 0 0.02' mass='0.1'/>
                    <geom type='box' size='0.02 0.008 0.028' pos='0.006 0 0.026' zaxis='1 0 -1'  mass='0.1'/>
                    <geom type='box' size='0.02 0.008 0.01' pos='0.02 0 0.01'  mass='0.1'/>
                    <geom type='box' size='0.04 0.008 0.02' pos='0 0 0.0'  mass='0.1'/>
                </body>
            </worldbody>
        </mujoco>
    """
)
class GHand:
    pass