import math
import matplotlib.pyplot as plt



# def vecteur_unitaire(P1,P2):
#     Ux = P2[0]-P1[0]
#     Uy = P2[1]-P1[1]
#     norme = math.sqrt(Ux*Ux+Uy*Uy)
#     if norme!=0:
#         return [Ux/norme,Uy/norme]
#     else:
#         return False

# def test_alignement_4pts(points,epsilon):
#     U1 = vecteur_unitaire(points[0],points[1])
#     U2 = vecteur_unitaire(points[1],points[2])
#     U3 = vecteur_unitaire(points[2],points[3])
#     if U2:
#         x = 2.0-(U1[0]*U2[0]+U1[1]*U2[1]+U2[0]*U3[0]+U2[1]*U3[1])
#     else:
#         x = 1.0-(U1[0]*U3[0]+U1[1]*U3[1])
#     if abs(x) < epsilon:
#         return True
#     else:
#         return False

# def division_courbe_bezier_3(points_control):
#     P01 = interpolation_lineaire(points_control[0],points_control[1],0.5)
#     P12 = interpolation_lineaire(points_control[1],points_control[2],0.5)
#     P23 = interpolation_lineaire(points_control[2],points_control[3],0.5)
#     P01_12 = interpolation_lineaire(P01,P12,0.5)
#     P12_23 = interpolation_lineaire(P12,P23,0.5)
#     Q = interpolation_lineaire(P01_12,P12_23,0.5)
#     return ([points_control[0],P01,P01_12,Q],[Q,P12_23,P23,points_control[3]])

# def courbe_bezier_3_recursif(points_control,epsilon,pile_points_courbe):
#     if test_alignement_4pts(points_control,epsilon):
#         pile_points_courbe.append(points_control[0])
#     else:
#         (points_1,points_2) = division_courbe_bezier_3(points_control)
#         courbe_bezier_3_recursif(points_1,epsilon,pile_points_courbe)
#         courbe_bezier_3_recursif(points_2,epsilon,pile_points_courbe)

# def courbe_bezier_3_recursif_init(points_control,epsilon):
#     pile_points_courbe = []
#     courbe_bezier_3_recursif(points_control,epsilon,pile_points_courbe)
#     pile_points_courbe.append(points_control[-1])
#     return pile_points_courbe
