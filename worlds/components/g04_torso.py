from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC


@interface()
class GTorsoInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-torso',
    components=[

    ],
    defaults={
        'mjc_interface': GTorsoInterfaceMJC
    },
    # language=xml
    template="""
        <mujoco>
            <worldbody>
<!--                <body pos='0 0 0.5'> -->
                    <geom type='sphere' size='0.1' pos='0 0 0.5'  mass='1'/>
                    
                    <body>
                        <geom type='box' size='0.15 0.08 0.08' pos='0 0 0.34' mass='1'/>
                        <geom type='box' size='0.11 0.06 0.1' pos='0 0 0.16' mass='1'/> 
                        <geom type='box' size='0.04 0.06 0.04' pos='0 0 0.04' mass='1'/> 
                    </body>
                    
                    
                    <body name='left-arm' pos='-0.2 0 0.4'/>
                    <body name='right-arm' pos='0.2 0 0.4'/>
                    
                    <body>
                        <joint name="left-hip-joint"/>
                        <body name='left-hip' pos='-0.1 0 0'/>
                    </body>
                    
                    <body>
                        <joint name="right-hip-joint"/>
                        <body name='right-hip' pos='0.1 0 0'/>
                    </body>
                <!-- </body> -->
            </worldbody>
        </mujoco>
    """
)
class GTorso:
    pass