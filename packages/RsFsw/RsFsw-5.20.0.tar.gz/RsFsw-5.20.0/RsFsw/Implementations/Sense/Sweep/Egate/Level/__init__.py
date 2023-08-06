from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def external(self):
		"""external commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_external'):
			from .External import ExternalCls
			self._external = ExternalCls(self._core, self._cmd_group)
		return self._external

	@property
	def ifPower(self):
		"""ifPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ifPower'):
			from .IfPower import IfPowerCls
			self._ifPower = IfPowerCls(self._core, self._cmd_group)
		return self._ifPower

	@property
	def rfPower(self):
		"""rfPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfPower'):
			from .RfPower import RfPowerCls
			self._rfPower = RfPowerCls(self._core, self._cmd_group)
		return self._rfPower

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel \n
		Snippet: driver.sense.sweep.egate.level.set(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:SWEep:EGATe:LEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel \n
		Snippet: value: float = driver.sense.sweep.egate.level.get() \n
		No command help available \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:LEVel?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'LevelCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LevelCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
