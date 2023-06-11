from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC


@interface()
class GHandInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-arm',
    components=[

    ],
    defaults={
        'mjc_interface': GHandInterfaceMJC
    },
    # language=xml
    template="""
        <mujoco>
            <worldbody>
                <body  pos='0 0 0.28'>
                    <geom type='capsule' size='0.03 0.1' pos='0 0 0.15'  mass='1'/>
                </body>
                
                <geom type='capsule' size='0.03 0.1' pos='0 0 0.15'  mass='1'/>

                <body name='wrist' pos='0 0 0.6'/>
            </worldbody>
        </mujoco>
    """
)
class GArm:
    pass