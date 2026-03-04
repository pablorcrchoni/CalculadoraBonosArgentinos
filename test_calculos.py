#!/usr/bin/env python3
"""
Script de prueba para la Calculadora de Bonos
Ejecuta simulaciones para validar que todo funciona correctamente
"""

import sqlite3
import json
from main import calcular_rendimientos, init_db, DATABASE

def prueba_calculos():
    """Ejecuta pruebas de cálculo sin interfaz web"""
    print("\n" + "="*60)
    print("🧪 PRUEBAS DE CALCULADORA DE BONOS")
    print("="*60 + "\n")

    # Inicializar BD
    try:
        init_db()
        print("✓ Base de datos inicializada\n")
    except Exception as e:
        print(f"✗ Error inicializando BD: {e}\n")
        return

    # Caso de prueba 1: PR17 más atractivo
    print("📊 CASO 1: Dólar sube poco (PR17 más atractivo)")
    print("-" * 60)
    resultado1 = calcular_rendimientos(
        dolar_hoy=1045,
        dolar_diciembre=1100,  # Sube poco
        tir_pr17=42.5,
        paridad_dual=18.5
    )
    print(f"  Dólar: $1.045 → $1.100 ({resultado1['variacion_dolar']:.2f}%)")
    print(f"  PR17:  {resultado1['rendimiento_pr17']:.2f}%")
    print(f"  Dual:  {resultado1['rendimiento_dual']:.2f}%")
    print(f"  ✓ Mejor: {resultado1['mejor_opcion']}")
    print(f"  Break-Even: ${resultado1['breakeven_dolar']:.2f}\n")

    # Caso de prueba 2: Dual más atractivo
    print("📊 CASO 2: Dólar sube mucho (Dual más atractivo)")
    print("-" * 60)
    resultado2 = calcular_rendimientos(
        dolar_hoy=1045,
        dolar_diciembre=1400,  # Sube bastante
        tir_pr17=42.5,
        paridad_dual=18.5
    )
    print(f"  Dólar: $1.045 → $1.400 ({resultado2['variacion_dolar']:.2f}%)")
    print(f"  PR17:  {resultado2['rendimiento_pr17']:.2f}%")
    print(f"  Dual:  {resultado2['rendimiento_dual']:.2f}%")
    print(f"  ✓ Mejor: {resultado2['mejor_opcion']}")
    print(f"  Break-Even: ${resultado2['breakeven_dolar']:.2f}\n")

    # Caso de prueba 3: Escenario realista argentino
    print("📊 CASO 3: Escenario Realista ARG (Marzo 2026)")
    print("-" * 60)
    resultado3 = calcular_rendimientos(
        dolar_hoy=1045,
        dolar_diciembre=1200,  # Predicción moderada
        tir_pr17=42.5,
        paridad_dual=18.5
    )
    print(f"  Dólar: $1.045 → $1.200 ({resultado3['variacion_dolar']:.2f}%)")
    print(f"  PR17:  {resultado3['rendimiento_pr17']:.2f}%")
    print(f"  Dual:  {resultado3['rendimiento_dual']:.2f}%")
    print(f"  ✓ Mejor: {resultado3['mejor_opcion']}")
    print(f"  Break-Even: ${resultado3['breakeven_dolar']:.2f}\n")

    # Verificar base de datos
    print("💾 ESTADO DE LA BASE DE DATOS")
    print("-" * 60)
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Contar simulaciones
        cursor.execute("SELECT COUNT(*) FROM simulaciones")
        total = cursor.fetchone()[0]
        print(f"  Total de simulaciones almacenadas: {total}\n")
        
        conn.close()
    except Exception as e:
        print(f"  Error accediendo BD: {e}\n")

    print("="*60)
    print("✓ Pruebas completadas")
    print("="*60 + "\n")

    print("🚀 Próximo paso: ejecutar 'python main.py'")
    print("   Luego abre: http://localhost:5000\n")

if __name__ == '__main__':
    prueba_calculos()
