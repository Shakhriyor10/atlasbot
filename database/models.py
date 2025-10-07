from __future__ import annotations

from typing import List

from sqlalchemy import BigInteger, Boolean, Float, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    language: Mapped[str] = mapped_column(String(5), default="ru")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class State(Base):
    __tablename__ = "states"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_ru: Mapped[str] = mapped_column(unique=True)
    name_en: Mapped[str] = mapped_column(unique=True)
    name_uz: Mapped[str] = mapped_column(unique=True)
    position: Mapped[int] = mapped_column(default=0)  # Поле для сортировки
    cities: Mapped[List["City"]] = relationship(
        back_populates="state", cascade="all, delete-orphan"
    )


class City(Base):
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_ru: Mapped[str] = mapped_column(unique=True)
    name_en: Mapped[str] = mapped_column(unique=True)
    name_uz: Mapped[str] = mapped_column(unique=True)
    position: Mapped[int] = mapped_column(default=0)  # Поле для сортировки
    state_id: Mapped[int] = mapped_column(ForeignKey("states.id"))
    state: Mapped["State"] = relationship(back_populates="cities")
    districts: Mapped[List["District"]] = relationship(
        back_populates="city", cascade="all, delete-orphan"
    )


class District(Base):
    __tablename__ = "districts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    name_ru: Mapped[str]
    name_en: Mapped[str]
    name_uz: Mapped[str]
    latitude: Mapped[float] = mapped_column(Float, default=0.0)
    longitude: Mapped[float] = mapped_column(Float, default=0.0)
    numbers: Mapped[List["Number"]] = relationship(
        back_populates="district", cascade="all, delete-orphan"
    )
    city: Mapped["City"] = relationship(back_populates="districts")
    __table_args__ = (UniqueConstraint("city_id", "name_ru", name="_city_district_uc"),)


class Number(Base):
    __tablename__ = "numbers"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    district_id: Mapped[int] = mapped_column(ForeignKey("districts.id"))
    number: Mapped[str] = mapped_column(String(20), nullable=False)
    district: Mapped["District"] = relationship(back_populates="numbers")

    __table_args__ = (
        UniqueConstraint("district_id", "number", name="_district_number_uc"),
    )
