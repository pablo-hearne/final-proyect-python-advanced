"use client";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Pencil, CalendarPlus, Plus, PawPrint } from "lucide-react";

const patients = [
  {
    id: "PAC-001",
    name: "Max",
    species: "Perro",
    breed: "Golden Retriever",
    owner: "Carlos Martinez",
    registrationDate: "22/03/2026",
  },
  {
    id: "PAC-002",
    name: "Luna",
    species: "Gato",
    breed: "Siames",
    owner: "Maria Garcia",
    registrationDate: "21/03/2026",
  },
  {
    id: "PAC-003",
    name: "Rocky",
    species: "Perro",
    breed: "Bulldog Frances",
    owner: "Ana Lopez",
    registrationDate: "20/03/2026",
  },
  {
    id: "PAC-004",
    name: "Mimi",
    species: "Gato",
    breed: "Persa",
    owner: "Juan Rodriguez",
    registrationDate: "19/03/2026",
  },
];

export function PatientsTable() {
  return (
    <Card>
      <CardHeader className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10">
            <PawPrint className="h-5 w-5 text-primary" />
          </div>
          <CardTitle className="text-xl">Ultimos Pacientes Registrados</CardTitle>
        </div>
        <Button className="gap-2">
          <Plus className="h-4 w-4" />
          Nuevo Paciente
        </Button>
      </CardHeader>
      <CardContent>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[100px]">ID</TableHead>
              <TableHead>Nombre del Paciente</TableHead>
              <TableHead className="hidden md:table-cell">
                Especie/Raza
              </TableHead>
              <TableHead className="hidden sm:table-cell">
                Nombre del Dueno
              </TableHead>
              <TableHead className="hidden lg:table-cell">
                Fecha de Registro
              </TableHead>
              <TableHead className="text-right">Acciones</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {patients.map((patient) => (
              <TableRow key={patient.id}>
                <TableCell className="font-medium text-primary">
                  {patient.id}
                </TableCell>
                <TableCell>
                  <div className="flex items-center gap-3">
                    <div className="flex h-9 w-9 items-center justify-center rounded-full bg-muted">
                      <PawPrint className="h-4 w-4 text-muted-foreground" />
                    </div>
                    <span className="font-medium">{patient.name}</span>
                  </div>
                </TableCell>
                <TableCell className="hidden md:table-cell">
                  <div>
                    <p className="font-medium">{patient.species}</p>
                    <p className="text-xs text-muted-foreground">
                      {patient.breed}
                    </p>
                  </div>
                </TableCell>
                <TableCell className="hidden sm:table-cell">
                  {patient.owner}
                </TableCell>
                <TableCell className="hidden lg:table-cell">
                  {patient.registrationDate}
                </TableCell>
                <TableCell className="text-right">
                  <div className="flex items-center justify-end gap-2">
                    <Button
                      variant="ghost"
                      size="icon"
                      className="h-8 w-8 text-muted-foreground hover:text-primary"
                      aria-label={`Editar paciente ${patient.name}`}
                    >
                      <Pencil className="h-4 w-4" />
                    </Button>
                    <Button
                      variant="ghost"
                      size="icon"
                      className="h-8 w-8 text-muted-foreground hover:text-accent"
                      aria-label={`Registrar visita para ${patient.name}`}
                    >
                      <CalendarPlus className="h-4 w-4" />
                    </Button>
                  </div>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  );
}
