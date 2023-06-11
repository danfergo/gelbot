from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC

from worlds.components.g02_hand import GHand
from worlds.components.g03_arm import GArm
from worlds.components.g04_torso import GTorso
from worlds.components.g05_leg import GLeg
from worlds.components.g06_foot import GFoot


@interface()
class GCamInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-bot',
    defaults={
        'mjc_interface': GCamInterfaceMJC
    },
    components=[
    ],
    # language=xml
    template="""
        <mujoco>
        </mujoco>
    """
)
class GBot:
    pass
