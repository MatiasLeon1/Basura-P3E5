# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:31:05 2020

@author: jpsil
"""


from matplotlib.pylab import *
from matplotlib import cm
import os

# Funcion

def imshowbien(u,Nx,Ny,coords):
    imshow(u.T[Nx::-1,:],cmap=cm.coolwarm, interpolation='bilinear')
    cbar=colorbar(extend='both', cmap=cm.coolwarm)
    ticks=arange(0,35,5)
    ticks_Text=["{}°".format(deg) for deg in ticks]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(ticks_Text)
    clim(0,30)
    
    xlabel('b')
    ylabel('a')
    xTicks_N=arange(0,Nx+1,3)
    yTicks_N=arange(0,Ny+1,3)
    xTicks=[coords(i,0)[0] for i in xTicks_N]
    yTicks=[coords(0,i)[1] for i in yTicks_N]
    xTicks_Text=["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text=["{0:.2f}".format(tick) for tick in yTicks]
    xticks(xTicks_N,xTicks_Text,rotation='vertical')
    yticks(yTicks_N,yTicks_Text)
    margins(0.2)
    subplots_adjust(bottom=0.15)

def truncate(n,decimals=0):
    multiplier=10**decimals
    return int(n*multiplier)/multiplier

"""
HACER UNA FUNCION; ASI ES MAS FACIL DE EXPLICAR EN EL INFORME
"""
def temperatura_hormigon(a,b,Nx,Ny,Temperatura_inicial,T_S,T_IZ,T_IN,T_D,G_S,G_IZ,G_IN,G_D,Titulo_carpeta,Grafico):
    
    # Crea una carpeta para que sea más facil corregir, todos los frame del caso n estaran en la carpeta n
    os.mkdir(Titulo_carpeta)
    # Definimos geometria
    
    # a=1. # alto del dominio
    # b=1. # ancho del dominio
    
    # Nx=30 # numero de intervalos en X
    # Ny = 30 # numero de intervalos en Y
    
    dx = b/Nx # Discretización
    dy = a/Ny
    
    h=dx
    # Importante
    # dx y dy tienen que ser iguales
    
    if dx != dy:
        print("ERROR !! dx != dy")
        exit(-1) # -1 le dice al SO que el programa fallo.
    # print(f"dx: {dx}")
    
    # Funcion de conveniencia para calcular las coordenadas depunto (i,j)
    coords = lambda i,j:(dx*i,dy*j)
    """
    def coords(i,j):
        return dx*i,dy*j
    """
    x,y=coords(4,2)
    
    print(f"x: {x}")
    print(f"y: {y}")
    
      
        
        
        
        
    
    u_k = zeros((Nx+1,Ny+1), dtype=double) #dtype es el tipo de dato
    u_km1 = zeros((Nx+1,Ny+1), dtype=double) #dtype es el tipo de dato
    
    # Condición de borde inicial
    u_k[:,:]=Temperatura_inicial # 20 grados en todas partes
    
    
    # Parametros del problema (hierro)
    dt=0.01 # s
    K=79.5 #m^2/2
    c=450. #J/kg*C
    rho=7800. #kg/m^3
    alpha=K*dt/(c*rho*dx**2)
    
    # Informar cosas interesantes
    print(f"dt = {dt}")
    print(f"dx = {dx}")
    print(f"K = {K}")
    print(f"c = {c}")
    print(f"rho = {rho}")
    print(f"alpha = {alpha}")
    
    # Loop en el tiempo
    minuto=60.
    hora=3600.
    dia=24*3600.
    
    dt=1*minuto
    dnext_t=0.5*hora
    
    next_t=0
    framenum=0
    
    T=1*dia
    Days=1*T # Cuantos dias quiero simular
    
    # Vectores para acumular la temperatura en puntos interesantes
    P1 = zeros(int32(Days/dt))
    P2 = zeros(int32(Days/dt))
    P3 = zeros(int32(Days/dt))
    superficie = zeros(int32(Days/dt))
    
    
    
    
    
    # Loop en el tiempo
    for k in range(int32(Days/dt)):
        t = dt*(k+1)
        dias = truncate(t/dia,0)
        horas = truncate((t-dias*dia)/hora,0)
        minutos = truncate((t-dias*dia-horas*hora)/minuto,0)
        titulo = "k = {0:05.0f}".format(k)+ "t = {0:02.0f}d {1:02.0f}h {2:02.0f}m".format(dias,horas,minutos)

        print(titulo)
        
        
        #CB esenciales, se repiten en cada iteración
        # gradiente=5.
        # u_k[0,:]=10. #Borde izquierdo.
        # u_k[:,0]=0. #Borde inferior.
        # u_k[:,-1]=u_k[:,-2]-0*dy #Borde superior
        # # (f(x+dx)-f(x))/dx = algo
        # # (u_k[-1,:]-u_k[-2,:])/dx=-10 #gradiente del lado derecho
        
        # u_k[-1,:]=u_k[-2,:]-gradiente*dx #Borde derecho, gradiente = -10
        
        # SUPERIOR
        if T_S!="@":
            u_k[:,-1]=T_S
        else:
            u_k[:,-1]=u_k[:,-2]-G_S*dy #Borde superior
        # IZQUIERDO
        if T_IZ!="@":
            u_k[0,:]=T_IZ #Borde izquierdo.
        else:
            u_k[0,:]=u_k[-2,:]-G_IZ*dx
        # INFERIOR
        if T_IN!="@":
            u_k[:,0]=T_IN
        else:
            u_k[:,0]=u_k[:,-2]-G_IN*dy #Borde superior
        # DERECHO
        if T_D!="@":
            u_k[-1,:]=T_D #Borde izquierdo.
        else:
            u_k[-1,:]=u_k[-2,:]-G_D*dx
        
        
        # Loop en el espacio i=1...
        for i in range(1,Nx):
            for j in range(1,Ny):
                
                # Algoritmo de diferencias finitas 2-D para difusión
                
                # Laplaciano
                nabla_u_k=(u_k[i-1,j] + u_k[i+1,j] + u_k[i,j-1] + u_k[i,j+1] - 4*u_k[i,j])/h**2
                
                #Forward Euler
                u_km1[i,j] = u_k[i,j]+alpha*nabla_u_k
        
        # Avanza la solución a k+1
        u_k=u_km1
        
        # # CB de nuevo, para asegurar cumplimiento
        # gradiente=5.
        # u_k[0,:]=10. #Borde izquierdo.
        # u_k[:,0]=0. #Borde inferior.
        # u_k[:,-1]=u_k[:,-2]-0*dy #Borde superior
        # # (f(x+dx)-f(x))/dx = algo
        # # (u_k[-1,:]-u_k[-2,:])/dx=-10 #gradiente del lado derecho
        
        # u_k[-1,:]=u_k[-2,:]-gradiente*dx #Borde derecho, gradiente = -10
        
        
        # SUPERIOR
        if T_S!="@":
            u_k[:,-1]=T_S
        else:
            u_k[:,-1]=u_k[:,-2]-G_S*dy #Borde superior
        # IZQUIERDO
        if T_IZ!="@":
            u_k[0,:]=T_IZ #Borde izquierdo.
        else:
            u_k[0,:]=u_k[-2,:]-G_IZ*dx
        # INFERIOR
        if T_IN!="@":
            u_k[:,0]=T_IN
        else:
            u_k[:,0]=u_k[:,-2]-G_IN*dy #Borde superior
        # DERECHO
        if T_D!="@":
            u_k[-1,:]=T_D #Borde izquierdo.
        else:
            u_k[-1,:]=u_k[-2,:]-G_D*dx
        
        
        # Encuentro temperatura en puntos interesantes
        superficie[k] = u_k[int(Nx/2),-1]
        P1[k] = u_k[int(Nx/2),int(Ny/2)]
        P2[k] = u_k[int(Nx/2),int(3*Ny/4)]
        P3[k] = u_k[int(3*Nx/4),int(3*Ny/4)]
        
        
        
        #Grafico en d_next
        if t>=next_t:
            figure(1)
            imshowbien(u_k,Nx,Ny,coords)
            title(titulo)
            # la carpeta tiene que existir
            savefig(Titulo_carpeta+"/frame_{0:04.0f}.png".format(framenum))
            framenum+=1
            next_t+=dnext_t
            close(1)
    
    # Ploteo historia de temperaturas en los puntos de interes
    figure(2)
    plot(range(int32(Days/dt)), superficie, label='superficie')
    plot(range(int32(Days/dt)), P1, label='P1')
    plot(range(int32(Days/dt)), P2, label='P2')
    plot(range(int32(Days/dt)), P3, label='P3')

    title("Evolucion de temperatura en puntos")
    legend()
    
    show()
    savefig(f"{Titulo_carpeta}/Grafico_{Grafico}")

"""
                    COSAS QUE CAMBIAR SI SE QUIERE OTRO RESULTADO O CASO
"""

temperatura_hormigon(1., 1., 30, 30, 20., 0., 20., 20., 0., "@", "@", "@", "@", "Caso_1",1)


# GIF
import glob
from PIL import Image

import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# FRAME
fp_in = "Caso_1/frame_*.png"
fp_out = "Caso_1/GIF_caso_1.gif"

listaImagenes=sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)




